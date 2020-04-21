
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

'''


def lengthOfLastWord(strng):
	splitted_str=strng.split()
	if len(splitted_str)==0:
		return 0
	return (len(splitted_str[-1]))

print(lengthOfLastWord("I am here hell99 "))