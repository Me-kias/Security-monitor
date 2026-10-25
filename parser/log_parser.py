from datetime import datetime
import re


def parse_log(log):
    parts = log.split(maxsplit=2)

    if len(parts) < 3:
        return None

    try:
        timestamp = datetime.fromisoformat(parts[0]).isoformat()
    except ValueError:
        return None

    # Support both:
    # timestamp sshd[123]: message
    # timestamp hostname sshd[123]: message
    service_index = 1
    service_match = re.match(
        r"([A-Za-z0-9_.-]+)(?:\[\d+\])?:",
        parts[service_index]
    )

    if not service_match and len(parts) >= 3:
        service_index = 2
        service_match = re.match(
            r"([A-Za-z0-9_.-]+)(?:\[\d+\])?:",
            parts[service_index]
        )

    if not service_match:
        return None

    service = service_match.group(1)

    if service_index == 1:
        message = parts[2]
    else:
        message = parts[2].split(":", 1)[1].strip()

    username = None
    source_ip = None

    failed_match = re.search(
        r"Failed password for (?:invalid user )?(\S+) "
        r"from (\d{1,3}(?:\.\d{1,3}){3})",
        message
    )

    if failed_match and service == "sshd":
        username = failed_match.group(1)
        source_ip = failed_match.group(2)
        event_type = "failed_login"
    else:
        success_match = re.search(
            r"Accepted (?:password|publickey) for (\S+) "
            r"from (\d{1,3}(?:\.\d{1,3}){3})",
            message
        )

        if success_match and service == "sshd":
            username = success_match.group(1)
            source_ip = success_match.group(2)
            event_type = "successful_login"
        elif service == "sudo" and "COMMAND=" in message:
            username_match = re.search(r"\bUSER=(\S+)", message)
            username = username_match.group(1) if username_match else None
            event_type = "sudo_command"
        else:
            return None

    return {
        "timestamp": timestamp,
        "service": service,
        "username": username,
        "source_ip": source_ip,
        "event_type": event_type,
    }