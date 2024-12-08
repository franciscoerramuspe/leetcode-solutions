'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''

def isPowerOfFour(n: int) -> bool:
    def checkIsPowerOfFour(y):
        res = 4**y
        if res < n:
            return checkIsPowerOfFour(y+1)
        elif res == n:
            return True
        else:
            return False
    return checkIsPowerOfFour(0)
    

print(isPowerOfFour(16) == True)
print(isPowerOfFour(25)==False)
print(isPowerOfFour(1024)==True)
print(isPowerOfFour(-15)==False)