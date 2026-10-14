from detection.detection_engine import detect_suspicious_activity

def test_detect_five_failed_logins():
    events = [
        {
            "event_type": "failed_login",
            "timestamp": f"2026-10-14T10:00:{second:02d}",
            "source_ip": "192.0.2.25"
        }
        for second in [5, 15, 25, 35, 45]
    ]

    alerts = detect_suspicious_activity(events)

    assert len(alerts) == 1
    assert alerts[0]["source_ip"] == "192.0.2.25"
    assert alerts[0]["attempt_count"] == 5