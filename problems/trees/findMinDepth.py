'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''
def findMinDepth(root):
    if not root:
        return 0
    queue=deque()
    queue.append((root, 0))

    while queue:
        node, depth = queue.popleft()
        depth+=1
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth))
        if node.right:
            queue.append((node.right, depth))