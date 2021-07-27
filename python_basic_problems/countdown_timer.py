# Python Program to Create a Countdown Timer
import time
time_input = int(input("Enter the time in seconds:"))
minutes = time_input // 60
seconds = 60
for i in range(60):
    print(f"{minutes}:{seconds}")
    seconds -= 1
    time.sleep(1)
