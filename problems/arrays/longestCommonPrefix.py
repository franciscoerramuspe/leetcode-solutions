'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


s=['flow', 'flo', 'flying']
ans='fl'

get the length of the smallest word in s
iterate through that length
check that all the strings have the same letter in position i
if they don't, return word[:i-1]

Time: O(N^2)
Space: O(1)

s=['flow', 'flo', 'flying']
ans='fl'
smallest=3
curChar=o

'''

def longestCommonPrefix(s):
    if len(s) == 1:
            return s[0]
    smallest=float('inf')
    for word in s:
        smallest=min(smallest, len(word))
    
    ans=''
    
    for i in range(smallest):
        curChar=s[0][i]
        for word in s:
            if word[i] != curChar:
                return ans
        # all the words share the same letter
        # add the letter to ans
        ans+=curChar
    return ans