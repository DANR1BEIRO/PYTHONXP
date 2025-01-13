import time

myTime = int(input("Enter the time in seconds: "))

# range(start, stop, step)
# % (modulus) calculates the remainder when dividing counter by 60.
# If the dividend (counter) is less than the divisor (60), the 
# remainder will simply be counter itself.
# If counter = 45, then 45 % 60 = 45 (because 45 < 60).
for counter in range(myTime, 0, -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"{hours:2}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")