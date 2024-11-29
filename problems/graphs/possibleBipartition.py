'''
We want to split a group of n people (labeled from 1 to n) into two groups of any size. 

Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, 

return true if it is possible to split everyone into two groups in this way.

notes:
    - not every person from 1 to n has to dislike someone
    - [[1,2],[1,3],[2,3]], here the answer is false because we need 3 different groups to order them (1 does not like 2 nor 3)
    - for a 

we can have either two forced groups, try every possible combination to make everyone fit in the right place
if they dont fit, then we return false, or we can also make as many groups as needed to make them fit and return len(groups)==2
'''
from collections import defaultdict

def possibleBipartition(dislikes, n):
    graph = defaultdict(list)
    for ai, bi in dislikes:
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    group1, group2 = set(), set()
    visited = set()

    def dfs(node, prevGroup):
        if node in prevGroup:
            return False
        curGroup = group1 if prevGroup == group2 else group2
        if node in curGroup: 
            return True

        visited.add(node)  
        curGroup.add(node)  

        for neighbor in graph[node]:
            if not dfs(neighbor, curGroup):
                return False
        return True

    for i in range(1, n + 1):
        if i not in visited and i in graph: 
            if not dfs(i, group1):
                return False

    return True
               


print(possibleBipartition([[1,2],[1,3],[2,3]], 3))