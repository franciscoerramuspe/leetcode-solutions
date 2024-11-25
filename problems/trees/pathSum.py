'''
Given the root of a binary tree and an integer targetSum, 

return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

if tree =
            5
         4      6
       6   1  2   4
targetSum = 13
ans = true

if tree =
            5
         4      6
       6   1  2   4
targetSum = 16
ans = False

compute all the root to leaf sums
when you get to a leaf, return currentSum == targetSum

Time: O(N)
Space: O(N) as we store the function callstack

'''
def pathSum(root, targetSum):
    if not root:
            return False
    
    def hasSum(node, curSum):
        if not node:
            return
        curSum += node.val
        if not node.left and not node.right: # leaf node
            return curSum == targetSum
        return (hasSum(node.left, curSum) or hasSum(node.right, curSum))

    sumIsPresent = hasSum(root, 0)
    return sumIsPresent if sumIsPresent else False 
