#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
A = abs(number) % 10
if number < 0:
    A =-A
    print("Last digit of"+str(number)+"is" +str(A)+ "and is ")
if A > 5:
    print("greateer than 5")
elif A == 0:
    print("0")
else:
    print("less than 6 and not 0")
