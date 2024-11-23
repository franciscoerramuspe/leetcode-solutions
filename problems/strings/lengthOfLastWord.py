'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

split the word by spaces into a list, return length of words[-1]

Time: O(N), as we have to split the string
Space: O(N), as we are storing an array

however, in an interview they may ask me to optimize this (and likely to not use .split)
How can we do this optimization?
Start at the end of the string with two pointers, l and r
if both pointers are pointing at an space, move them together until they both find a character
when they both find a character, move the left backwards until it finds a new space
return r-l
example:
s = "   hi my    name is   francisco    "
                          l        r

s = 'a '
    lr

Time: O(N)
Space: O(1)
'''
def lengthOfLastWord(s):
    #First solution
    # words = s.split(' ')
    #     r = len(words)-1
    #     while True:
    #         if words[r]:
    #             return len(words[r])
    #         r-=1
    # if len(s) == 1:
    #     return 1

    # Second optimized solution
    l = r = len(s)-1
    while True:
        if s[r] != ' ':
            while s[l] != ' ' and l > 0:
                l-=1
            if l == 0 and s[l] != ' ':
                return r-l+1
            return r-l
        else:
            r-=1
            l-=1



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




test_cases = [
    (("Hello World",), 5),
    ((" a",), 1),
    (('a ', ), 1),
    (("   hi my    name is   francisco    ", ), 9)
]

if __name__ == "__main__":
    run_tests(lengthOfLastWord, test_cases)

