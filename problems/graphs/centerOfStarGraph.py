'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. 

A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 

Return the center of the given star graph.

given=[[4, 5], [3, 5], [2, 5]]
ans = 5

given=[[2, 1], [1,4], [3, 1], [1,5]]
ans = 1


find the node that is connected to every node (the node that appears in all [u, v] pairs)
check all u, v pairs
count num of ocurrences
return the node where it has n occurrences

Time:O(m*n)
Space:O(m*n)
'''
def centerOfStarGraph(edges):
    occurrences = {}
    for edge in edges:
        u, v = edge[0], edge[1]
        if u not in occurrences:
            occurrences[u] =1
        else:
            occurrences[u]+=1
        if v not in occurrences:
            occurrences[v] =1
        else:
            occurrences[v]+=1
    return max(occurrences, key=occurrences.get)

def check_eq(a, b):
    if a != b:
        print(f"Expected: {b}, Result: {a}")
        raise AssertionError(f"Test failed. Expected: {b}, but got: {a}")
    else:
        print("Test passed!")


print(check_eq(centerOfStarGraph([[2, 1], [1,4], [3, 1], [1,5]]), 1))
print(check_eq(centerOfStarGraph([[4, 5], [3, 5], [2, 5]]), 5))
