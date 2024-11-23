'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard 

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

row1: qwertyuiop
row2: asdfghjkl
row3: zxcvbnm

words = ["Hello", "Fran", "Gas", "Tero"]
output = 2

words = ["nico", "mate", "asado", "pizza", 'e']
output = 1

we can create a set with all the characters for fast lookup( O(1) ) for each row
the problem there, is that we have to go, character by character of each, checking if all the characters are present in one row

what we can also do is check the first character and be that one the one who dictates in which row we are looking
that is, for the word: Hello, we look at what row H belongs to, and we stick with that set for the rest of the characters

how do we deal with uppercase?
we either remove them from the input (change it to the lowercase version), or add them to the set (which I think it is better)


Time: O(n*m), where n is the number of words and c is the average number of chars of each word
Space: O(N), as we are storing a dictionary with all the chars. However, this space can also be considered constant, as it is the same regardless of the input
            that is, it is always going to be 26 * 2 chars stored and always 3 keys in the dict. So could be also considered O(1)
'''

def keyboardRow(words):
    selected = {
        1:set(('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P')),
        2:set(('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L')),
        3:set(('z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')),
    }
    
    curRow = 0
    ans = []
    fullWord = 0
    for word in words: 
        for char in word:  
            if not curRow: 
                if char in selected[1]:
                    curRow = 1
                elif char in selected[2]:
                    curRow = 2
                else:
                    curRow = 3
            if char not in selected[curRow]:
                break
            fullWord+=1 
        if fullWord == len(word):
            ans.append(word)
        fullWord = 0
        curRow = 0
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
    ((["Hello", "Fran", "Gas", "Tero"],), ["Gas", "Tero"]), 
    ((["nico", "mate", "asado", "pizza", 'e'],), ["e"]), 
]

if __name__ == "__main__":
    run_tests(keyboardRow, test_cases)