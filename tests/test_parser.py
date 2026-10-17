from parser.log_parser import parse_log
def test_failed_login():
    # Arrange
    log = "2026-10-08T12:00:00+00:00 mint sshd: Failed password for admin from 10.0.2.20"

    # Act
    event = parse_log(log)

    # Assert
    assert event["event_type"] == "failed_login"
    assert event["username"] == "admin"
    assert event["source_ip"] == "10.0.2.20"

def test_invalid_log():
    log = "this is not a valid log"

    event = parse_log(log)
    assert event is None
    
def test_successful_login():
    log = "2026-10-08T12:00:00+00:00 mint sshd: Accepted password for admin from 10.0.2.20"
    event = parse_log(log)
    assert event["event_type"] == "successful_login"
    assert event["username"] == "admin"
    assert event["source_ip"] == "10.0.2.20"