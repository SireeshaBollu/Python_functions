"""Take three user inputs and print the greatest number from those inputs
using if-else condition. Edge cases, if any, should also be handled.
"""
#Conditional Statement

def print_highest_number(a,b,c):
	if a>b and a>c:
		print("A is greater")
	elif b>c and b>a:
		print("B is greater")
	elif c>a and c>b:
		print("C is greater")
	else:
		print("A is equal to B is equal to C")

print_highest_number(100, 100, 100)
