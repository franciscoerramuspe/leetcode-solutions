'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 

If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

nums=[2, 4, 7, 8, 11, 14]
target=13
ans=-1

nums=[2, 5, 6, 7, 8, 10, 11]
target=11
ans=6

'''
def findTargetInSortedArray(nums, target):
    l, r = -1, len(nums)

    while r-l>1:
        m=(r+l)//2
        if nums[m] >= target:
            r=m
        else:
            l=m
    if r <len(nums) and nums[r] == target:
        return r
    else:
        return -1

def cheq_eq(a,b):
    if a==b: print('test passed')
    else: print('test failed')

print(cheq_eq(findTargetInSortedArray([2, 4, 7, 8, 11, 14], 13), -1))
print(cheq_eq(findTargetInSortedArray([2, 5, 6, 7, 8, 10, 11], 11), 6))

    

