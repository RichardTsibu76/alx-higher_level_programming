#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number >= 0):
    last_digit = number % 10
else:
    import math
    last_digit = math.fmod(number, 10)
if (last_digit > 5):
    print("Last digit of {} is {} and is greater than 5".format("number", last_digit))
if (last_digit == 0):
    print(f"Last digit of {number} is {last_digit} and is 0")
elif (last_digit != 0 and last_digit < 6):
    print(f"""Last digit of {number} is {last_digit:.0f} \
and is less than 6 and not 0""")
