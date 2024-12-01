'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

A subset of an array is a selection of elements (possibly none) of the array.

The solution set must not contain duplicate subsets. Return the solution in any order.

for array =[1, 2, 3]
ans=[[], [1], [1,2], [1, 2, 3], [1,3], [2], [2, 3], [3]]

the size of ans would be 2^len(array)
for each character, we have two choices:
    - not pick the current char
    -pick the cur char

we can use a backtracking approach to track the index of the current iteration
retun if we get to the n index

Time:O(2^n)
Space:O(n)
'''
def subsets(nums):
    ans=[]
    n=len(nums)
    def generateSubsets(i, curSubset):
        if i == n:
            ans.append(curSubset.copy())
            return
        generateSubsets(i+1, curSubset)
        curSubset.append(nums[i])
        generateSubsets(i+1, curSubset)
        curSubset.pop()
    generateSubsets(0, [])
    return ans 

print(subsets([1, 2, 3]))
