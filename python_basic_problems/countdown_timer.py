# Python Program to Create a Countdown Timer
import time
minutes = int(input("Enter the time in minutes:"))
# minutes = time_input / 60
seconds = 60
for i in range(minutes * 60):
    print(f"{minutes - 1}:{seconds}")
    seconds -= 1
    if seconds == 0:
        seconds = 60
        minutes -= 1
    time.sleep(1)
