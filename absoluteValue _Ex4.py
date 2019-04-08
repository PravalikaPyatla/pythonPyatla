#!/usr/bin/env python3
import random
# calculate absolute value
def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""
    #return abs(num)
	if num >= 0:
		return num
	else:
		return -num

num1 = random.randint(-50,50)
print("Number 1 :")
print(num1)
print("Absolute value:")
print(absolute_value(num1))
num2 = random.randint(-50,50)
print("Number 2 :")
print(num2)
print("Absolute value:")

print(absolute_value(num2))