"""Create an array that has user defined inputs and with the help of for loop,
fetch all the prime numbers and print the numbers.
"""

def check_prime_number(input_num):
	for i in range(2, input_num):
		if input_num % i == 0:
			return False
	return True

my_array = []
try:
	a = int(input("Please input a number or Enter 0 to exit...\n"))
except ValueError:
	print("Please input a valid number")
	a = int(input("Please input a number or Enter 0 to exit...\n"))

while a:
	my_array.append(a)
	a = int(input("Please input a number or Enter 0 to exit...\n"))

print(my_array)
result = []


for i in my_array:
	if check_prime_number(i):
		result.append(i)

print(f"Prime numbers are /n - {result}")


