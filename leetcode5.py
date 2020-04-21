'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''

def addDigits(num):
	sum_ = 0
	while(num>=10):
		for k in str(num):
			sum_ += int(k)
		return sum_
print(addDigits(17118))