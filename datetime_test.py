from datetime import datetime

timestamp1 = "2026-10-08T12:00:00+00:00"
timestamp2 = "2026-10-08T12:01:30+00:00"

time1 = datetime.fromisoformat(timestamp1)
time2 = datetime.fromisoformat(timestamp2)

difference = time2 - time1

print(difference)
print(difference.total_seconds())