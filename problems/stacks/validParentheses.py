'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

s='((()))
true

s={[)}
false

s=([{}])
true

have a dictionary of closed to open 
every time we find an open parentheses we add to the stack
if we find a closed one, check the dictionary where the key is the closed one we just found
if the top of the stack does not match with the value of the dictionary that we are referencing to, then return false
else pop from the stack and keep going
at the end, if the stack is empty return true, else false

Time:O(N)
Space:O(N) 

'''
def validParentheses(s):
    if len(s) ==1:
            return False
        
    closedToOpen={
        ')':'(',
        ']':'[',
        '}':'{'
    }

    stack = []

    for char in s:
        # it is a closed parentheses
        if char in closedToOpen:
            if not stack:
                return False
            elif closedToOpen[char] == stack[-1]:
                stack.pop()
            else:
                return False
        # it is an open parentheses
        else:
            stack.append(char)
    return not stack



def check_eq(a,b):
    assert a==b, print(f"Expected: {a}\nResult:{b}")


# Example Test Cases
test_cases = [
    ("()", True),
    ("(]", False),
    ("[{}]", True),
    ("[", False),
    ("", True),
    ("{[()]}", True),
    ("{[(])}", False),
]

# Run tests
for s, expected in test_cases:
    result = validParentheses(s)
    check_eq(result, expected)

print("All test cases passed!")