'''

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,

which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Time: O(mxn)
Space: O(mxn)
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distances = [[float("inf")] * (cols+1) for r in range(rows+1)]
        distances[rows-1][cols]=0

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                distances[r][c] = grid[r][c] + min(distances[r+1][c], distances[r][c+1])
        return distances[0][0]