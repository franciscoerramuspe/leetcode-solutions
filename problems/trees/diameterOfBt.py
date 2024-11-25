'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


if tree =
            5
         4      6
       6   1  2   4
ans = 4

if tree =
            5
         4      6
       6   1
         2   4
        7 5
       3
ans=5
longestPath=[6, 4, 1, 2, 7, 3]

calculate all the leaf to leaf paths, return the length of the path. 
Have a variable that tracks the max length of the paths. Return once we finished checking all leaf to leaf paths

        
'''

def diameterOfBt(root):
    largestDiameter = [0]

    def getDiameter(node):
        if not node:
            return 0
        
        left = getDiameter(node.left)
        right = getDiameter(node.right)

        curDiameter = left + right
        largestDiameter[0] = max(curDiameter, largestDiameter[0])
        
        return 1+ max(left, right)
    
    getDiameter(root)

    return largestDiameter[0]