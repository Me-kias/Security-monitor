from datetime import datetime, timedelta


def detect_suspicious_activity(events):
    failed_logins = {}
    alerts = []

    for event in events:
        if event["event_type"] != "failed_login":
            continue
        timestamp = datetime.fromisoformat(event["timestamp"])
        source_ip = event["source_ip"]

        if source_ip is None:
            continue

        if source_ip not in failed_logins:
            failed_logins[source_ip] = []

        failed_logins[source_ip].append({
            "timestamp": timestamp,
            "event": event
        })

    for source_ip, attempts in failed_logins.items():
        attempts.sort(key=lambda attempt: attempt["timestamp"])

        for i in range(len(attempts)):
            window_start = attempts[i]["timestamp"]
            window_end = window_start + timedelta(seconds=120)

            matching_attempts = [
                attempt for attempt in attempts
                if window_start <= attempt["timestamp"] <= window_end
            ]
            if len(matching_attempts) >= 5:
                alerts.append({
                    "alert_type": "repeated_failed_logins",
                    "source_ip": source_ip,
                    "attempt_count": len(matching_attempts),
                    "description": (
                        f"{len(matching_attempts)} failed login attempts "
                        f"from {source_ip} within 120 seconds"
                    )
                })
                break
    return alerts