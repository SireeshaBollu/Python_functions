"""We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
 We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
"""
def are_we_introuble(a_smile, b_smile):
	if a_smile == b_smile:
		return True
	else:
		return False


 		
 
print(are_we_introuble(True, False))