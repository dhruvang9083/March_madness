'''
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.
'''


def isPalindrome(number):
	if str(number) == str(number)[::-1]:
		return True
	else:
		return False 

print(isPalindrome(-111))