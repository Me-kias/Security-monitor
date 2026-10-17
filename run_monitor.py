from collector.log_reader import read_logs
from parser.log_parser import parse_log
from detection.detection_engine import detect_suspicious_activity
from database.alert_storage import create_database, save_alert, get_alerts


def run_monitor():
    print("Starting AI-Assisted Cybersecurity Monitor...")

    # 1. Make sure the database and alerts table exist.
    create_database()

    # 2. Read and parse the authentication logs.
    events = []

    for log in read_logs():
        event = parse_log(log)

        if event is not None:
            events.append(event)

    print(f"Parsed {len(events)} security events.")

    # 3. Detect suspicious activity.
    alerts = detect_suspicious_activity(events)

    # 4. Save newly detected alerts.
    for alert in alerts:
        save_alert(alert)
        print("ALERT:", alert["description"])

    # 5. Show a summary.
    print(f"New alerts generated: {len(alerts)}")

    stored_alerts = get_alerts()
    print(f"Total alerts stored: {len(stored_alerts)}")


if __name__ == "__main__":
    run_monitor()