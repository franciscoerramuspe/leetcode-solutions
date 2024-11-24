'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



s = 'aba'
true

s = 'absa'
true

s = 'bafre'
false 

string can be empty
just english lowercase letters

s = s a b a
    l     r

almost a palindrome= a string that has an etxra character that prevents the string to be a palindrome
if i am in a position where two chars are different, compare, s[l+1] to s[r], if they are equal, delete s[l],
otherwise, if s[r-1] == s[l], then delete r, and decrement charsToBeDeleted
keep going with the regular palindrome approach while checking that charsToBeDeleted is >= 1 whenever we find a different character
if it's < 1 return false
return true if the pointers meet each other

Time: O(N)
Space: O(1)

solution failed with test case: s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
(passed 463/474) test cases


'''
def validPalindrome2(s):
    # second solution that passes all test
    if not s:
        return False
    if len(s) == 1:
        return True
    l, r = 0, len(s) -1
    def checkPalindrom(l, r, charsToBeDeleted):
        while l < r: # lcupuufxxfuupucul, l = p, r = p, charsToBeDeleted = 1
            if s[l] != s[r]:
                if not charsToBeDeleted:
                    return False
                if s[l+1] == s[r] and s[r-1] == s[l]: 
                    charsToBeDeleted-=1
                    return (checkPalindrom(l+1, r, 0) or checkPalindrom(l, r-1, 0))
                elif s[l+1] == s[r]:
                    charsToBeDeleted-=1
                    l+=1
                elif s[r-1] == s[l]: # delete s[r]
                    charsToBeDeleted-=1
                    r-=1
                else:
                    return False
            r-=1
            l+=1
        return True
    return checkPalindrom(l, r, 1)

    # first solution that passed 463/474 tests
    '''
    class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
        if len(s) == 1:
            return True
        charsToBeDeleted = 1
        l, r = 0, len(s) -1

        while l < r: # saba, l = a, r = a, charsToBeDeleted = 0
            if s[l] != s[r]:
                if not charsToBeDeleted:
                    return False
                elif s[l+1] == s[r]: # delete s[l]
                    charsToBeDeleted -=1
                    l+=1
                elif s[r-1] == s[l]: # delete s[r]
                    charsToBeDeleted-=1
                    r-=1
                else:
                    return False
            r-=1
            l+=1
        return True

    '''


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
    (('saba',), True),
    (('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga',), True),
    (('lcupuufxxfuupucul',), True),
    (('agucbbcga',), True)
    
]

   

if __name__ == "__main__":
    run_tests(validPalindrome2, test_cases)