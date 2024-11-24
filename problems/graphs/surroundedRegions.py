'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

repharase problem: 
    given an mxn matrix containing of Xs and Os, 
    find each surrounded region(set of adjacent cells horizontally or vertically) of Os that cannot be on the edges
    explore each region. If the region is fully surrounded with X's, mark that region as surrounded
    once you explore all regions, traverse the surrounded ones and turn the Os to Xs
    return the grid


'''
def surroundedRegions(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()

    def getRegion(r, c, curRegion):
        if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and matrix[r][c] == 'O':
            visited.add((r, c))
            curRegion.add((r, c))
            getRegion(r+1, c, curRegion)
            getRegion(r-1, c, curRegion)
            getRegion(r, c+1, curRegion)
            getRegion(r, c-1, curRegion)
        return curRegion
            
    
    def isSurrounded(region):
        for r, c in region:
            #check if the region touces the edge
            if 0 == r  or r == rows-1 or 0== c or c == cols-1:
                return False
        return True
    
    regions = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'O' and (r, c) not in visited:
                regions.append(getRegion(r, c, set()))
    
    for region in regions:
        if isSurrounded(region):
            for r, c in region:
                matrix[r][c] = 'X'

    return matrix





def run_tests(func, test_cases):
    for i, (input_board, expected_board) in enumerate(test_cases):
        try:
            # Create a deep copy of the input_board to avoid modifying the test case
            board_copy = [row[:] for row in input_board]
            
            # Call the function with the board copy
            func(board_copy)
            
            # Compare the modified board with the expected output
            assert board_copy == expected_board, (
                f"Test case {i + 1} failed:\n"
                f"Input: {input_board}\n"
                f"Expected Output: {expected_board}\n"
                f"Actual Output: {board_copy}"
            )
            print(f"Test case {i + 1} passed ✅")
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"Test case {i + 1} encountered an error: {e}")

# Corrected test_cases
test_cases = [
    (
        [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]],
        
        [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]],
    ),
    (
        [["X"]],
        [["X"]]
    ),
    (
        [["O","O","O"],
        ["O","O","O"],
        ["O","O","O"]],
       
       [["O","O","O"],
        ["O","O","O"],
        ["O","O","O"]]
    ),
]

   

if __name__ == "__main__":
    run_tests(surroundedRegions, test_cases)
