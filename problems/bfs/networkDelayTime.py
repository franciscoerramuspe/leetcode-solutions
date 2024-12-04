'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),

where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

we need to use dijkstras:
    - we need to create a graph with an adjacency list, in which for each node, we store the its adjacent nodes along with their respectives distances
    - priority queue, returns the node with the closest distance
    - we need a map that will serve as a visited+distance track, since if we are visiting a node for the 2nd time, we want to make sure we keep its shortest distance

start from src and go to all of its neighbors
    - if they are not visited, add them to the visited+distance map and the distance it took to get there
    - if they are visited, check the previosu distance and compare it with the current one. Store the smaller one, skip the other one



'''
from collections import defaultdict
import heapq
def networkDelayTime(times, n, k):
    graph=defaultdict(list)
    visitedAndDistance=defaultdict(int)
    pq=[(0, k)]
    heapq.heapify(pq)
    
    for src, destination, distance in times: # construct graph with its distances
        graph[src].append((destination, distance))
    
    while pq:
        curDistance, curNode = heapq.heappop(pq)
        if curNode in visitedAndDistance:
                continue
        visitedAndDistance[curNode]=curDistance
        if curNode in graph:
            for neighbor in graph[curNode]:
                neighborVal, neighborDistance= neighbor
                if neighborVal not in visitedAndDistance:
                    heapq.heappush(pq, (curDistance+neighborDistance, neighborVal))

    latestNode=max(visitedAndDistance, key=visitedAndDistance.get) # key with the highest value
    return visitedAndDistance[latestNode] if len(visitedAndDistance) == n else -1
        
print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2)
print(networkDelayTime([[2,1,1]], 2, 2) == -1)
print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2)