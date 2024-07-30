
#IF-else statement
	"""Input the values of a and b as 10 and 20 respectively. Now check if a is
greater or b is greater using if condition. Think about all the edge cases,
and print the statements accordingly.
"""


from decimal import Decimal
def compare_numbers(a, b):
	if a is None:
		print("Please input a proper value for a")
		return
	if b is None:
		print("Please input a proper value for b")
		return
	if not isinstance(a,  (int, Decimal, float)):
		print("a should be any one of the int , decimal , float")
		return
	if not isinstance(b,  (int, Decimal, float)):
		print("b should be any one of the int , decimal , float")
		return
	if a>b:
		print("A is greater")
	elif b>a:
		print("B is greater")
	else:
		print("A is equal to B")

compare_numbers("1", 2)