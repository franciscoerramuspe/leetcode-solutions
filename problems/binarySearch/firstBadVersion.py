'''
'''
# version 1 (sin la receta)
 def firstBadVersion(self, n: int) -> int:
        if n==1:
            return n
        l, r = 1, n

        while l<=r:
            m=(r+l)//2
            if isBadVersion(m):
                r=m-1
            else:
                l=m+1
        return l

#version 2 (con la receta)
def firstBadVersion(self, n: int) -> int:
        a = 0
        b = n + 1 
        while b - a > 1:
            c = (a + b) // 2
            if isBadVersion(c):
                b = c
            else:
                a = c

        # b es la primera version mala (si es que existe)
        if b <= n and isBadVersion(b):
            return b
        return -1 