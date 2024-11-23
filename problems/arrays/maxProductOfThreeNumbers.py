'''
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

nums = [4, 3, 5, 9, 10, 2]

ans = 9*10*5
 what if we have two very large negative numbers and one very large positive?

 nums = [-5, -4, -1, 0, 1, 4, 5]
 ans = -5*-4*5
 ans = 100

brute force: triple nested for loop. Not optimal since its time is O(n^3)

sort the array, maxProduct will be the maximum value of: 
    - the product of the three largest nums
    or
    - the product of the two smallest values and the largest

Time: O(nlgn) as we have to sort the array
Space: O(1) if we dont consider the input
'''
def maxProductOfThreeNums(nums):
    nums = sorted(nums)
    maxProduct = max(
        (nums[-1]*nums[-2]*nums[-3]),
        (nums[0]*nums[1]*nums[-1])
    )
    return maxProduct
    

    



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
    ([[4, 3, 5, 9, 10, 2],], 450),
   ]

# Run tests
if __name__ == "__main__":
    run_tests(maxProductOfThreeNums, test_cases)