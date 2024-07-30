"""
	The parameter weekday is True if it is a weekday, and 
	We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""


def sleep_in(weekday, vacation):
	return not weekday or vacation


	# if weekday and not vacation:
	# 	return False
	# elif weekday and vacation:
	# 	return True
	# else:
	# 	return True



result = sleep_in(False, False)

if result:
	print("padukunta")
else:
	print("padukonu")

#IF-else statement
	"""Input the values of a and b as 10 and 20 respectively. Now check if a is
greater or b is greater using if condition. Think about all the edge cases,
and print the statements accordingly.
"""


a = 10;
b = 20;
if a>b :
	print("A is greater")
else:
	print("B is greater")


"""Take three user inputs and print the greatest number from those inputs
using if-else condition. Edge cases, if any, should also be handled.
"""
#Conditional Statement

a = 100;
b = 200;
c = 300;
if a>b :
	print("A is greater")
elif b>c:
	print("B is greater")
elif c>a:
	print("C is greater")
else:
	print("A is equal to B is equal to C")



	#Print the numbers from 1 to 10 using while loop

number = 1
while number <= 10:
    print(number)
    number += 1


    """Create a list that has 10, 23, 4, 26, 4, 75, 24, 54 values and with the help
of while loop fetch the even numbers and print the number
"""


#Creating the list with the name called numbers
numbers = [10, 23, 4, 26, 4, 75, 24, 54]
index = 0    #assigning the indexing to the list
while index < len(numbers):    #iterating the while loop
    if numbers[index] % 2 == 0:  # Check if the number is even
        print(numbers[index])     # Print the even number
    index += 1  # Increment the counter



    """Create an array that has user defined inputs and with the help of for loop,
fetch all the prime numbers and print the numbers.
"""





        #Write a program that takes a positive integer 𝑁 as input and prints the first N natural numbers.
n = int(input("Enter the positive integer:"))
for i in range(1,n+1):
	print(i)






	










