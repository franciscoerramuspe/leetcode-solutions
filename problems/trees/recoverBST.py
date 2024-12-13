'''
You are given the root of a binary search tree (BST),

where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
'''


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def getValues(node):
            if not node:
                return
            
            getValues(node.left)
            heapq.heappush(heap, node.val)
            getValues(node.right)
        heap=[]
        heapq.heapify(heap)
        getValues(root)

        def changeValues(node):
            if not node:
                return
            
            changeValues(node.left)
            orderedVal=heapq.heappop(heap)
            if node.val != orderedVal:
                node.val = orderedVal
            changeValues(node.right)

        changeValues(root)
        return root