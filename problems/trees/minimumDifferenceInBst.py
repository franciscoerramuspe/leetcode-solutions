'''
Given the root of a Binary Search Tree (BST),

return the minimum absolute difference between the values of any two different nodes in the tree.

        5
      3   6
    2  4    8
ans =1

        5
      2   8
            14
ans =3

        5
      5   6
    2  4    8
ans =0


    5
   2  4
   minVal=1

'''
from colelctions import deque
def minimumDifferenceInBst(root):
    #optimal
    prevNodes=[]
        minVal=[float('inf')]
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if not prevNodes:
                prevNodes.append(node.val)
            else:
                minVal[-1]=min(minVal[-1], abs(node.val-prevNodes[-1]))
                prevNodes.append(node.val)
            dfs(node.right)
        dfs(root)
        return minVal[-1]

    #brute force
    # q=deque(root)
    # values=[]
    # minVal=float('inf')
    # while q:
    #     curNode=q.popleft()
    #     values.append(curNode.val)

    #     if curNode.left:
    #         q.append(curNode.left)

    #     if curNode.right:
    #         q.append(curNode.right)
    
        
    # for i in range(len(values)):
    #     for j in range(i+1, len(values)):
    #         curDiff=abs(values[i]-values[j])
    #         minVal=min(minVal, curDiff)
    # return minVal

