'''
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
    
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

                  i  j
nums1 = [1, 2, 2, 2, 0, 4, 5]
         k  
nums2 = [2, 4, 5]
m = 4
n = 3

we need three pointers: one at the end of the nonzero nums of nums1 (i), another at the end of nums1 (j), and a last one at the end of nums2 (k)
we would compare nums1[i] and nums2[k]. We would assign the bigger value between these two to nums1[j]. 
We will decrease the pointer of the value we assigned to nums1[j], and repeat this process while k>=0.


Time: O(n+m)
Space: O(1)

'''
def mergeArrays(nums1, nums2, m, n):
    i, j, k = m - 1, m + n - 1, n - 1

    while k >= 0:
        if i >= 0 and nums2[k] > nums1[i]:
            nums1[j] = nums2[k]
            k -= 1
        elif i >= 0:
            nums1[j] = nums1[i]
            i -= 1
        else:
            nums1[j] = nums2[k]
            k -= 1
        j -= 1
    return nums1
    # first solution (was failing the second test)
    # i, j, k = m-1, m+n-1, n-1
    # while k >= 0:
    #     if nums2[k] > nums1[i]:
    #         nums1[j]= nums2[k] 
    #         j-=1
    #         k-=1
    #     elif nums2[k] < nums1[i]:
    #         nums1[j] = nums1[i]
    #         j-=1
    #         i-=1
    #     else:
    #         nums1[j] = nums2[k]
    #         j-=1
    #         k-=1
    


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
    (([1, 2, 2, 3, 0, 0, 0], [2, 3, 5], 4, 3), [1, 2, 2, 2, 3, 3, 5]),
     (([2, 0], [1], 1, 1), [1, 2]),
   ]

   

if __name__ == "__main__":
    run_tests(mergeArrays, test_cases)