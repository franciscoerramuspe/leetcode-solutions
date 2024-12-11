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