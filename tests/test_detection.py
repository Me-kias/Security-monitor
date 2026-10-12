from detection.detection_engine import detect_suspicious_activity

def test_detect_suspicious_activity():
    events = [
        {"event_type": "failed_login", "username": "admin", "source_ip": "10.0.2.20"},
        {"event_type": "successful_login", "username": "admin", "source_ip": "10.0.2.20"},
        {"event_type": "failed_login", "username": "guest", "source_ip": "10.0.2.30"},
        {"time_stamp": "2026-10-08T12:00:00+00:00"},
        ]
    result = detect_suspicious_activity(events)
    assert len(result) == 2

    