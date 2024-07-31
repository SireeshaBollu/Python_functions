"""Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string
(i.e. n will be in the range 0..len(str)-1 inclusive)."""

a = "abcdef"

# result = ""
# for index, value in enumerate(a):
# 	if index == 3:
# 		continue
# 	result = result + value


# print(result)

a = list(a)
del a[2]  # delete a particular index
# print(a)
a.remove('f')  # actual character name
a = ''.join(a)
print(a)

