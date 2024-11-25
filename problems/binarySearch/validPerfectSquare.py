'''
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.


16
l, r = 1, 7
m = 4

if m * m > num:
    r=m-1

'''
def isValidSquare(num):
    l, r = 1, num

    while l <= r:
        m = (r+l) //2
        curSquare = m*m
        if curSquare > num:
            r = m-1
        elif curSquare < num:
            l = m+1
        else:
            return True
    return False





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
    ((16,), True),
    ((64,), True),
    ((5,), False),
]



if __name__ == "__main__":
    run_tests(isValidSquare, test_cases)