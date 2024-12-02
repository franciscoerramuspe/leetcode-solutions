'''
Given an array nums of distinct integers, return all the possible permutations
You can return the answer in any order.

A permutation is a rearrangement of all the elements of an array.

Time:O(N!)
Space:O(N) (function callstack)
'''
def permutations(nums):
    ans, curPermutation =[], []
    def getPermutations():
        if len(curPermutation) == len(nums):
            ans.append(curPermutation.copy())
            return
        for num in nums:
            if num not in curPermutation:
                curPermutation.append(num)
                getPermutations() #this allows us to create lists in all orders such as (2, 1, 3)
                curPermutation.pop() # once we get to the base case (line 13), we come back here to pop and use a different permutation (this is the backtracking part)
    getPermutations()
    return ans
print(permutations([1, 2, 3]))
            