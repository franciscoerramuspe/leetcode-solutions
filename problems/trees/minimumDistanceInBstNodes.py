'''
Given the root of a Binary Search Tree (BST), 
return the minimum difference between the values of any two different nodes in the tree.


'''
# solution 1, did not work for all test cases
# def minDistanceBst(root):
#     if not root:
#         return None
    
#     queue=deque()
#     queue.append((root))
#     minDiff=float('inf')

#     while queue:
#         node=queue.popleft()
#         if node.left:
#             curDiff= abs(node.val-node.left.val)
#             minDiff=min(minDiff, curDiff)
#             queue.append(node.left)
#         if node.right:
#             curDiff= abs(node.val-node.right.val)
#             minDiff=min(minDiff, curDiff)
#             queue.append(node.right)
#     return minDiff

# solution 2, works but it is O(n^2 time)
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue=deque()
        queue.append((root))
        minDiff=float('inf')
        nodes=[]
        while queue:
            node=queue.popleft()
            nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                curDiff=abs(nodes[i]-nodes[j])
                minDiff=min(minDiff, curDiff)
        return minDiff


#tests: [4,2,6,1,3], ans =1
# tests: [1,0,48,null,null,12,49], ans =1
# tests: [90,69,null,49,89,null,52], ans =1