'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

condition to evaluate if 3 sides can create a valid triangle:
Each pair of sides must sum to more than the third side.
in other words, for sorted(a, b, c)
a+b > c


[2,3,4,6]

[2,3,4] is valid
[3,4,6]is valid

             i  j  k
[2, 3, 4, 5, 6, 6, 7]
is valid:
[2, 3, 4]
[3,4, 6]
[3,4,6]
[4,5,6]
[4,5,6]
[3,5,6]
[3,5,6]
[4,5,6]
[4,5,6]
[4,6,7]
[4,6,7]
[5,6,7]
[5,6,7]

construct an array isValid for each pair of triplets
have two pointers (i, j) where they start at 0 and 1 respectfully
have a pointer k that starts at j+1 and check the function isValid(a,b,c), 
if it returns true: ans+=1
else: i=j, j=j+1, k=j+1


'''
# tuve que leer las soluciones para poder sacar esta solucion
def triangleNumber(nums: List[int]) -> int:
    def isValidTriangle(triplet):
        return triplet[0]+triplet[1]>triplet[2]
    
    nums.sort()
    n = len(nums)
    if n<3:
        return  0
    
    ans = 0
    for c in range(2, n):
        a, b = 0, c-1
        while b-a>0:
            if isValidTriangle([nums[a], nums[b], nums[c]]):
                ans+= (b-a)
                b-=1
            else:
                a+=1
    return ans


    # esta fue mi primer solucion que intente (y no funcionó)
    # def isValid(triplet):
    #     triplet=sorted(triplet)
    #     return triplet[0]+triplet[1]>triplet[2]
    
    # if len(nums)==3:
    #     return 1 if isValid(nums) else 0
    
    # i, j, k=0, 1, 2
    # ans = 0
    # while i < len(nums)-2:
    #     curTriplet=[nums[i], nums[j], nums[k]]
    #     isTriangle=isValid(curTriplet)
    #     if isTriangle:
    #         ans+=1
    #     if k==len(nums)-1:
    #         #we finsished exploring all the possibilites for nums[i]
    #         i+=1
    #         j=i+1
    #         k=j+1
    #     else:
    #         k+=1
    #         j+=1
    # return ans
        

def cheq_eq(a,b):
    if a==b:
        print('test Passed')
    else:
        print('test failed')

cheq_eq(isValidTriangle([2,3,4,6]), 2)