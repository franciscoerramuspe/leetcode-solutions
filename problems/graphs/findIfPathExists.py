'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 

The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.

Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

perform dfs from starting node. If target is found return true
if we run out of nodes to explore or we find the source again return false

edges=[[0,3], [3,2] [2, 0], [1,2]]
source=0
destination=1
ans = true

since we have an array we can construct a graph with a default dict
'''
from collections import defaultdict
def findIfPathExist(edges, n, source, destination):
    if not edges:
            return True
    graph = defaultdict(list)
    for ui, vi in edges:
        graph[ui].append(vi)
        graph[vi].append(ui)

    visited = set()
    def findPath(node, target):
        if node not in visited:
            visited.add(node)
            if node == target:
                return True
            for children in graph[node]:
                if findPath(children, target):
                    return True
        

    for edgePair in edges:
        for edge in edgePair:
            if edge == source:
                if findPath(edge, destination):
                    return True
    return False

def cheq_eq(a, b):
    if a == b:
        print('test passed')
    else:
        print('test failed')

edges = [[0, 1], [1, 2], [2, 3]]
n = 4
source = 0
destination = 3
expected = True

edges1 = [[0,3], [3,2], [2, 0], [1,2]]
n1 = 4
source1 = 0
destination1 = 1
expected1 = True



print(cheq_eq(findIfPathExist(edges, n, source, destination), expected))
print(cheq_eq(findIfPathExist(edges1, n1, source1, destination1), expected1))

