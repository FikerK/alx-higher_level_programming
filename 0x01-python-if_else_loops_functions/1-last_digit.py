#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ld = number % -10
else:
    ld = number % 10
if ld > 5:
    txt = "and is greater than 5"
elif ld == 0:
    txt = "and is 0"
elif ld < 6 and ld != 0:
    txt = "and is less than 6 and not 0"
print('Last digit of', number, 'is', ld, txt)
