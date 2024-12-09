'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Time: O(N)
Space: O(N)
'''

#solucion 1 (no pasa todos los casos)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque()
        queue.append((root, 'l'))
        ans = []

        while queue:
            curLevel=[]
            levelSize=len(queue)
            for _ in range(levelSize):
                node, prevSide = queue.popleft()
                curLevel.append(node.val)

                if prevSide == 'l': # right first for the next
                    if node.right:
                        queue.append((node.right, 'r'))
                    if node.left:
                        queue.append((node.left, 'r'))
                else: # left first for the next
                    if node.left:
                        queue.append((node.left, 'l'))
                    if node.right:
                        queue.append((node.right, 'l'))
            ans.append(curLevel.copy())
            
        return ans


# solucion 2: me costo bastante llegar a esta pero una vez que pensé en usar otra forma de clasificar los niveles se me hizo mas facil
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque()
        queue.append((root, 1))
        ans = []

        while queue:
            curLevel=[]
            levelSize=len(queue)
            for _ in range(levelSize):
                node, prevLevel = queue.popleft()
                curLevel.append(node.val)
                if node.right:
                    queue.append((node.right, prevLevel+1))
                if node.left:
                    queue.append((node.left,prevLevel+1))

            if prevLevel %2==1:
                curLevel=curLevel[::-1]
            ans.append(curLevel.copy())

               
        return ans