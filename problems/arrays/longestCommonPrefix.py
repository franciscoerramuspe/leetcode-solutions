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

# intento 2 hacer con trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.trie=TrieNode()

    def insert(self, word):
        trie=self.trie
        for char in word:
            if char not in trie.children:
                trie.children[char]=TrieNode()
            
            trie=trie.children[char]
        trie.is_end_of_word=True

    def startsWith(self, prefix):
        trie=self.trie
        for c in prefix:
            if c not in trie.children:
                return False
            trie=trie.children[c]
        return True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        ans=''
        trie=trie.trie
        while True:
            if len(trie.children) != 1 or trie.is_end_of_word:
                return ans
            
            for char, nxt in trie.children.items():
                ans+=char
                trie=nxt
        return ans
        
