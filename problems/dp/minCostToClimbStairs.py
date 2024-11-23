'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.

Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

[2, 4, 5, 1, 2, 6]

res = 2 + 4 + 1 + 2


[10, 15, 20]
res = 15

[10, 15, 20]


get all the possible answers and return the smallest one?

However, we can compute the min cost to get to the ith position

and to get to the position i, we always want to pick the minimum of the positions i-1 and i-2

we can start by building up a dp array with the two starting costs (nums[0] and nums[1])

and then compute nums[i] based on whichever is cheaper from both

at the end, return the cheapest position to jump to the top (n-1 or n-2)

time: O(N)
Space: O(N)


'''

def minCostToClimbStairs(nums):
    dp = [nums[0], nums[1]] # this array represents the minimum cost to get to position i
    n = len(nums)
    for i in range(2, n):
        dp.append(min(dp[-1]+nums[i], dp[-2]+nums[i]))
    return min(dp[-1], dp[-2])
            


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
    ([[10, 15, 20],], 15),
    ([[2, 4, 5, 1, 2, 6],],7),
    ([[1,100,1,1,1,100,1,1,100,1],],6)
   ]

   

if __name__ == "__main__":
    run_tests(minCostToClimbStairs, test_cases)