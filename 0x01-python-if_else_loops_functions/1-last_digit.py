#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = abs(number) % 10
result_string = "The string Last digit of " + str(number) + " is " + str(last_digit) + " and is "
if last_digit > 5:
    result_string += "greater than 5"
elif last_digit == 0:
    result_string += "0"
else:
    result_string += "less than 6 and not 0"
print(result_string)
