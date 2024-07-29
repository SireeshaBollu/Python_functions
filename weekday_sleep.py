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

