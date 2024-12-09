'''
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. 

You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.


rooms=[[0,4], 
       [4,4]]
ans=6
in 4 seconds you can start moving to the next room
moving room takes one second (t=5)
in one second move out of room (1,1)

therefore, for each room, t+= ((rooms[i][1]-rooms[i][0]) +1)

Input: moveTime = [[0,0,0],
                   [0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second

Input: moveTime = [[0,1],[1,2]]
in t=2 you are at 1,0

Output: 3


'''