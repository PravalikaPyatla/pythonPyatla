#!/usr/bin/env python3

# calculate absolute value
def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		return num
	else:
		return -num


print(absolute_value(2))

print(absolute_value(-4))