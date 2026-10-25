
from datetime import datetime
import re


def parse_log(log):
    parts = log.split(maxsplit=3)

    if len(parts) < 3:
        return None

    # Parse the ISO timestamp used by Linux Mint.
    try:
        timestamp = datetime.fromisoformat(parts[0]).isoformat()
    except ValueError:
        return None

    # Extract the service name, such as sshd or systemd-logind.
    service_match = service_match = re.match(r"([A-Za-z0-9_.-]+)(?:\[\d+\])?:", parts[1])
    if not service_match:
        return None

    service = service_match.group(1)
    message = parts[3]

    username = None
    source_ip = None

    # Failed SSH authentication.
    failed_match = re.search(
        r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})",
        message,
    )

    if failed_match and service == "sshd":
        username = failed_match.group(1)
        source_ip = failed_match.group(2)
        event_type = "failed_login"

    else:
        # Successful SSH password or public-key authentication.
        success_match = re.search(
            r"Accepted (?:password|publickey) for (\S+) from (\d{1,3}(?:\.\d{1,3}){3})",
            message,
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
