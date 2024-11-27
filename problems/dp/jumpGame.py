'''
You are given an integer array nums. 

You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

nums = [2, 0, 1, 3, 0, 1, 1]
true

nums = [1, 0, 1, 0, 0, 1, 1]
false

try all possible jumps with the current number
avoid zeroes
return true if you are able to get to the end, false if you are stuck in an index
'''

def jumpGame(nums):
   # Greedy approach -> Time O(N), Space: O(1)
    n = len(nums)
    target = n-1

    for i in range(n-1, -1, -1):
       maxJump = nums[i]
       if i + maxJump >= target:
           target = i
    return target == 0

# DP solution
def jumpGameDp(nums):
    dp = [False for _ in range(len(nums))]
    dp[-1] = True 

    for i in range(len(nums)-2, -1, -1):
        #  iterate through all possible jumps from i and update dp[i] to True if any of those positions can reach the end.
        for jump in range(1, nums[i] + 1):
            newIndex=i+jump
            if newIndex < len(nums):
                if dp[newIndex]:
                    dp[i]=True
                    break
        else:
            dp[i]=False
    return dp[0]


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
    ([[2, 0, 1, 3, 0, 1, 1],], True),
    ([[1, 0, 1, 0, 0, 1, 1],], False),
    ([[3,2,1,0,4],], False)

   ]

   

if __name__ == "__main__":
    run_tests(jumpGameDp, test_cases)