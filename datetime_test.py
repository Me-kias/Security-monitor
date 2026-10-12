from datetime import datetime

time1 = datetime.strptime("10:00:00", "%H:%M:%S")
time2 = datetime.strptime("10:01:30", "%H:%M:%S")

difference = time2 - time1

print(difference)