'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.


[1, 1, 1, 0],
[1, 1, 0, 0],
[0, 1, 0, 1],


when we find an island, we want to look at all of his neighbors using bfs in the 4 directions
when we look in the 4 directions and the adjacent nodes are either visited or 0, then we want to flip that 0 into 1


'''
from collections import deque
def shortestBridge(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    ans=0
    
    def dfs(r, c):
        if 0<= r < rows and 0 <= c < cols and matrix[r][c] == 1 and (r, c) not in visited:
            visited.add((r, c))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r+dr, c+dc)
        return
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1 and (r, c) not in visited:
                start = dfs(r, c)
                break
        if visited:
            break
    
    
    queue = deque(visited)

    while queue:
        for _ in range(len(queue)): # we increment ans after processing all nodes in this layer
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r+dr, c+dc
                if 0<= newR < rows and 0 <= newC < cols and (newR, newC) not in visited:
                    if matrix[newR][newC] == 1:
                        return ans
                    else:
                        visited.add((newR, newC))
                        queue.append((newR, newC))
        ans+=1
            


matrix=[[1, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 1]]
print(shortestBridge(matrix) == 1)
    
