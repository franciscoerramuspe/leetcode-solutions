'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

given [1, 2, 3, 4, 5]
ans = 
        3
      2    4
    1        5

given [-6, -3, -1, 2, 5, 6]
ans = 
            -1
          -3   5
        -6    2  6

given [-6, -3, -1, 0, 1, 2, 5, 6]

ans = 
        1
     -3     5
    -6 -1  2  6
         0

find the middle node (if it is an even list chose whichever of the two middle nodes)
the middle node would be the root of the tree. All the values to the right would go on the righ children, all the values to the left would go on the left children
repeat this process until no more nodes should be added

Time: O(N) where N is all the nums in the array
Space: O(N) as we create a tree structure of N nodes
'''
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left=left
        self.right=right
    
class Solution:
    def sortedArrayToBst(self, nums):
        def createBst(nums):
            if not nums:
                return
            middle = len(nums)//2
            node = Node(val=nums[middle])

            leftSubtree = nums[:middle]
            rightSubtree = nums[middle+1:]
            
            node.left=createBst(leftSubtree)
            node.right=createBst(rightSubtree)
            return node

    
        bst = createBst(nums)
        return bst
