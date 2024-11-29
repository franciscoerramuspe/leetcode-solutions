'''
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. 

If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
[1, 2, 4, 5, 6]
[3, 4, 8]
ans = 4

[1, 2, 4, 5, 6]
[3, 7, 8]
ans = -1

[1, 2, 4, 5, 6]
[1]
ans = 1


for binary search we have a target. What if we grab the list with the smallest length.
We go one by one for each num in that list, and we run binary search on the other list and try to find that number
if we dont find it, we move to the next element in the smaller list
if all the nums in the smaller list are not found return -1
else return the first one you find

time:O(k lg n) where k is the length of the smaller list

'''
def minimumCommonValue(nums1, nums2):
    def isNumPresent(nums, target):
        a, b = -1, len(nums)
        while b-a>1:
            c=(a+b)//2
            if nums[c]>=target:
                b=c
            else:
                a=c
        if b < len(nums) and nums[b] == target:
            return True
        else:
            return False
    
    for num in nums2:
        if isNumPresent(nums1, num):
            return num
    return -1

def cheq_eq(a,b):
    if a==b:print('test case passed')
    else: print('test cassed failed')


print(cheq_eq(minimumCommonValue([1, 2, 4, 5, 6], [3, 4, 8]), 4))
print(cheq_eq(minimumCommonValue([1, 2, 4, 5, 6], [3, 7, 8]), -1))
print(cheq_eq(minimumCommonValue([1, 2, 4, 5, 6], [1]), 1))