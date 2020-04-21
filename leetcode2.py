'''

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

'''


def searchInsert(lst, target):
	if target in lst:
	    return lst.index(target)
	else:
	    lst.append(target)
	    lst.sort()
	    return lst.index(target)


print(searchInsert([11,3,2,5,4],6))
print(searchInsert([11,3,2,5,4],0))
print(searchInsert([11,3,2,5,4],20))