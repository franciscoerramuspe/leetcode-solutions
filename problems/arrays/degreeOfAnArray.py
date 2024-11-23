'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

rephrase: 
    given nums
    degree = max_freq of element -> if 3 has a freq of 5 and its the highest freq, then degree = 5
    goal=smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.


Input: nums = [1,2,2,3,1]
Output: 2
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

tasks:
    - get the degree of nums ( the number(num) with highest freq(k))
    - given that degree, find the smallest window in which we can find k times num
    - return length of that window

nums = [1, 2, 5, 5, 6, 7, 5, 5]
n = 5, k =4
goal= find a window with four 5s
two pointers (l, r), start from 0, 0
if both of these pointers are different from num, increase both
the goal is that l starts from the very first occurrence of num
expand pointer r while k > 0, decrement k as we find num
return r-l


Time: O(n * k), where n is the number of distinct numbers in the array, and k is the number of total elements in the array
Space: O(2 k) -> O(k), where k is the number of total elements in the array
'''

def degreeOfArray(nums):
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num]+=1
    
    max_value = max(counter.values())
    # Get all key-value pairs with the highest value
    results = [(key, value) for key, value in counter.items() if value == max_value]
    
    ans=float("inf")
    for result in results:
        num, k = result[0], result[1]
        l, r = 0, 0
        while k > 0:
            # [1,2,2,3,1]
            if nums[l] != num and nums[r] != num:
                l+=1
                r+=1
            elif nums[r] == num and nums[l] == num:
                k-=1
                r+=1
            else:
                r+=1
        ans=min(r-l, ans)
    return ans
        
   

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
    (([1, 2, 5, 5, 6, 7, 5, 5],), 6),
    (([2, 2, 2, 2],), 4),
    (([1],), 1),
    (([8, 2, 4, 8, 8, 3, 9, 8, 8],), 9),
    (([1,2,2,3,1],), 2),
    (([1,1, 1, 1, 4, 4, 4, 4, 3, 3, 3, 3],), 4)


    
]

if __name__ == "__main__":
    run_tests(degreeOfArray, test_cases)