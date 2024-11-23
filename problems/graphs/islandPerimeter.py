'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 

The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

[
 [0, 1, 0],
 [0, 1, 0],
 [1, 1, 1]
 ]
 perimeter = 3 + 2 + 3 + 1 + 3 = 12
 perimeter = for each one we find, we can add at most 4 units to the perimeter. However, for each adjacent one, we will subtract 1 from the 4.

 For example, in the given example, the one in matrix[2][1] just has a value of 1, because it has 3 adjacent ones, the one at matrix[1][1] has a value of 2
 For this problem: 
    - keep track of visited cells
    - traverse the matrix until we find the first 1 (the beginning of the island)
    - once we find it, traverse the matrix from that one in the directions up, down, left, right
    - for that cell, we would return 4 - number of ones attached (len of stack)
    - we will recursively call this function and add to the total result for each call.
    - Time: O(m * n), where m is the num of rows and n is the num of cols
    - Space: O(m * n), as we would be storing tuples of coordinates for each row visited
    
    '''
def islandPerimeter(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = set()
    island_perimeter = 0
    stack = []

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 1 and (r, c) not in visited:
                stack.append((r, c))
                while stack:
                    i, j = stack.pop()
                    if (i, j) in visited:
                        continue

                    visited.add((i, j))
                    cell_perimeter=4

                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        new_row, new_col = i+dr, j+dc
                        if 0 <= new_row < m and 0 <= new_col < n:
                            if matrix[new_row][new_col] == 1:
                                cell_perimeter -= 1 
                                if (new_row, new_col) not in visited:
                                    stack.append((new_row, new_col))
                    island_perimeter += cell_perimeter
    
    return island_perimeter


def run_tests(func, test_cases):
    for i, (inputs, expected) in enumerate(test_cases):
        try:
            if isinstance(inputs, dict):
                result = func(**inputs)
            else: 
                result = func(*inputs)

            # Check if the result matches the expected output
            assert result == expected, f"Test case {i + 1} failed: {inputs} -> Expected {expected}, but got {result}"

            print(f"Test case {i + 1} passed ✅")
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"Test case {i + 1} encountered an error: {e}")




# Add test cases here
test_cases = [
    ([[[0, 1, 0], [0, 1, 0],[1, 1, 1]],], 12),
        ([[[1]],], 4),
        ([[[1,0]],], 4),
        ([[[1, 0, 0],[1, 0, 0],[1, 1, 1]],],12)
   ]

# Run tests
if __name__ == "__main__":
    run_tests(islandPerimeter, test_cases)