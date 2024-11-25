'''
You have n coins and you want to build a staircase with these coins. 

The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

if n = 6

rows = [1, 2, 3]
ans = 3

if n = 5
rows = [1, 2, 2]
ans = 2 because the third row is not complete

start at 1. while n > 0, add a new row using the following rules:
    - if n >= rows[i-1]+1 
        rows[i] = rows[i-1]+1
        totalRows+=1
        n-=rows[i]
    - else:
         rows[i] = n
Time: O(n)
Space: O(1)
I came up with the first solution, watched a video after to see the math formula behind it 
'''

def arrangeCoins(n):
    if n < 1:
            return 0
    lastRow=1
    n-=1
    totalRows=1
    while n>0: 
        if n >= lastRow+1:
            lastRow=lastRow+1
            n-=lastRow
            totalRows+=1
        else:
            lastRow = n
            n -= lastRow
    return totalRows

# math formula
# def arrangeCoins(n):
#     return int((-1+ sqrt(1+8*n))//2)

def run_tests(func, test_cases):
    for i, (inputs, expected) in enumerate(test_cases):
        try:
            if isinstance(inputs, dict):
                result = func(**inputs)
            else:
                result = func(*inputs)

            assert result == expected, f"Test case {i + 1} failed: {inputs} -> Expected {expected}, but got {result}"

            print(f"Test case {i + 1} passed ✅")
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"Test case {i + 1} encountered an error: {e}")

test_cases = [
    ((5,), 2),
]



if __name__ == "__main__":
    run_tests(arrangeCoins, test_cases)