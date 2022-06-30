#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
word = str()
if number < 0:
    last = -1 * last
if last > 5:
    word = "and is greater than 5"
elif last < 6 and last != 0:
    word = "and is less than 6 and not 0"
else:
    word = "and is 0"
print(f"Last digit of {number} is {last} {word}")
