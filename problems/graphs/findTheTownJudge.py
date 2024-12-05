'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody. (there is no edge from the judge to another node)
Everybody (except for the town judge) trusts the town judge. (there are n-1 nodes with a directed edge to the judge)
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

there should be n-1 edges directed to a node to be the town judge
that node cannot be a key in the graph




[[1,2], [3, 2], [4, 2], [5,2]]

        1  5  4   3
            2


ans = 2

[[1,2], [2, 3], [3,4]]
ans = -1

[[2,1]]
ans =1

construct a graph

Time complexity:O(n.m)
Space complexity:O(n.m)

'''
from collections import defaultdict
def findTheTownJudge(trust, n):
    if n == 1:
            return 1
    if not trust:
        return -1
        
    graph = defaultdict(list)
    
    for ui, vi in trust:
        graph[ui].append(vi)
    
    trustCounter = defaultdict(int)
    for ui, trusts in graph.items():
        for trusting in trusts:
            trustCounter[trusting] += 1
    
    for person in range(1, n + 1):
        if trustCounter[person] == n - 1 and person not in graph:
            return person
        
    return -1
def cheq_eq(a,b):
    if a==b: print('test case passed')
    else: print('test case failed')

print(cheq_eq(findTheTownJudge([[1,2], [3, 2], [4, 2], [5,2]], 5), 2))
print(cheq_eq(findTheTownJudge([[1,2], [2, 3], [3,4]], 4), -1))
print(cheq_eq(findTheTownJudge([[2,1]], 2), 1))
print(cheq_eq(findTheTownJudge([[1,2], [2, 3], [3,4]], 4), -1))
print(cheq_eq(findTheTownJudge([[]], 1), 1))