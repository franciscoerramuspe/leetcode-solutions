'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Time: O(N)
Space: O(N)
'''

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        counter={}
        queue=deque()
        queue.append(root)

        while queue:
            node=queue.popleft()

            if node.val in counter:
                counter[node.val]+=1
            else:
                counter[node.val]=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        mode=max(counter, key=counter.get)
        maxVal=counter[mode]
        ans=[key for key, val in counter.items() if val == maxVal]
                
        return ans


        # tests
        # input: [4, 3, 5, 1, null, 6], ans= [4, 3, 5, 1, 6]
        # input: [4, 2, 7, 1, 2, 7, 9, null, null, 9], ans= [7, 9]
        # input: [6, 3, 8, 3, 4], ans= [3]
        #input:  [1], ans=[1]