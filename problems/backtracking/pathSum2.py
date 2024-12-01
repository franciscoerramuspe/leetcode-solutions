'''
Given the root of a binary tree and an integer targetSum, 

return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 

Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

we need a helper function getPath that gets all the paths from root to leaf
as we traverse the tree, if we get to a leaf and pathSum == target, then we add that path to the ans
if it doesnt, then we have to backtrack and explore the remaining root-to-leaf paths
repeat until we ran out of root to leaf paths to traverse

input:
        2
      3   4
    1  5 3  4

target: 10
ans=[[2,3,5], [2,4,3]]

Time: O(N)
Space: O(N) 
'''
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    def getPath(node, curPath):
        if not node:
            return
        curPath.append(node.val)
        if not node.left and not node.right:
            if sum(curPath) == targetSum:
                ans.append(curPath.copy())
        else:
            getPath(node.left, curPath)
            getPath(node.right, curPath)
        curPath.pop()
        
    ans = []
    getPath(root, [])
    return ans
    