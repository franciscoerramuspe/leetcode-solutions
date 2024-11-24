'''
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer.
 
A character can only be typed if the pointer is pointing to that character.

The pointer is initially pointing to the character 'a'.

Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.

Type the character the pointer is currently on.

Given a string word, return the minimum number of seconds to type out the characters in word.

word = 'abc'
ans = 5

word='acz'
ans= 1+(2+1)+(3+1)

therefore, we can conclude that, for each character, we would add to the answer in the following way:
    (minDistanceToCharacterFromCurCharacter+1)

given that we have clockwise and counterclockwise traversals, we can isolate the logic of returning minDistance in a function
and then call that function to get the distance, add 1 to that result, and add that addition to the ans

Time: O(N) as we go through every character in word
Space: O(1)
'''

def typewriter(word):
    def getMinDistance(startChar, endChar):
        startPos = ord(startChar) - ord('a')
        endPos = ord(endChar) - ord('a')
        forwardDistance = (endPos - startPos) % 26
        backwardDistance = (startPos - endPos) % 26
        return min(forwardDistance, backwardDistance)
    
    ans = 0
    prevChar = 'a'
    for char in word:
        ans += (getMinDistance(prevChar, char) + 1)
        prevChar = char
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
    (('acz',), 8),
    (('abc',), 5),
    (('bza',), 7),
    (('zjpc',), 34),

    
    
]

   

if __name__ == "__main__":
    run_tests(typewriter, test_cases)
