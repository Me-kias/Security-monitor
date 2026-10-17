from datetime import datetime
import re


def parse_log(log):
    parts = log.split()

    if len(parts) < 5:
        return None

    # Convert the syslog timestamp into ISO format.
    try:
        timestamp = datetime.strptime(
            " ".join(parts[:3]) + f" {datetime.now().year}",
            "%b %d %H:%M:%S %Y"
        ).isoformat()
    except ValueError:
        return None

    # In standard syslog lines, the service follows the hostname.
    service = parts[4].split("[")[0].strip(":")

    username = None

    if "Failed password" in log:
        username_match = re.search(
            r"Failed password for (?:invalid user )?(\S+)", log
        )
        if username_match:
            username = username_match.group(1)

        event_type = "failed_login"

    elif "Accepted password" in log or "Accepted publickey" in log:
        username_match = re.search(
            r"Accepted (?:password|publickey) for (\S+)", log
        )
        if username_match:
            username = username_match.group(1)

        event_type = "successful_login"

    elif "sudo" in log:
        event_type = "sudo_command"

    else:
        return None

    ip_match = re.search(
        r"\bfrom (\d+\.\d+\.\d+\.\d+)\b", log
    )
    source_ip = ip_match.group(1) if ip_match else None

    return {
        "timestamp": timestamp,
        "service": service,
        "username": username,
        "source_ip": source_ip,
        "event_type": event_type
    }
