import sys

from collector.log_reader import read_logs
from parser.log_parser import parse_log
from detection.detection_engine import detect_suspicious_activity
from database.alert_storage import create_database, save_alert, get_alerts


def run_monitor(log_file=None):
    print("Security Monitor...")
    create_database()

    events = []
    raw_line_count = 0
    skipped_line_count = 0

    logs = read_logs(log_file) if log_file else read_logs()
    for log in logs:
        raw_line_count += 1
        event = parse_log(log)

        if event is not None:
            events.append(event)
        else:
            skipped_line_count += 1

    print(f"Raw log lines read: {raw_line_count}")
    print(f"Parsed security events: {len(events)}")
    print(f"Unrecognized log lines: {skipped_line_count}")

    alerts = detect_suspicious_activity(events)

    for alert in alerts:
        save_alert(alert)
        print("ALERT:", alert["description"])

    print(f"New alerts generated: {len(alerts)}")

    stored_alerts = get_alerts()
    print(f"Total alerts stored: {len(stored_alerts)}")


if __name__ == "__main__":
    run_monitor(sys.argv[1] if len(sys.argv) > 1 else None)
