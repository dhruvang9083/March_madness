'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

'''

def removeDuplicates(nums):
	nums.sort()
	i=1
	while( i<len(nums)):
		if(nums[i-1]==nums[i]):
			nums.pop(i)
			continue
		i+=1
	print(nums)
	return len(nums)

print(removeDuplicates([0,4,6,2,3,4,1]))