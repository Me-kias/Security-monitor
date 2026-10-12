from datetime import datetime


def detect_suspicious_activity(events):
    failed_logins = {}

    for event in events:
        if event["event_type"] == "failed_login":
            timestamp = datetime.fromisoformat(event["timestamp"])
            source_ip = event["source_ip"]

            if source_ip not in failed_logins:
                failed_logins[source_ip] = []

            failed_logins[source_ip].append({
                "timestamp": timestamp,
                "event": event
            })

    return failed_logins