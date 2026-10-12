from datetime import datetime

timestamp = "2026-10-08T12:00:00+00:00"
time = datetime.fromisoformat(timestamp)

print(time)