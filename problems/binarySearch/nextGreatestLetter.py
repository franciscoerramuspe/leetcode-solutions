'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 
 use the binary search formula
 Time:O(lg n)
 Space:O(lg n) for the function call stack. Can be done in O(1) if instead of the function the calculation is made in-place 

'''

def nextGreatestLetter(letters, target):
    def isCharGreaterThanTarget(c):
        return c>target
    
    l, r = 0, len(letters)-1
    while l<=r:
        m = (r+l) // 2
        if isCharGreaterThanTarget(letters[m]):
            r=m-1
        else:
            l=m+1

    return letters[l] if l < len(letters) else letters[0]