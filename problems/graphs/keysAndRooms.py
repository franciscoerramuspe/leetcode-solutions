'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. 

However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. 

Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

rooms=[[2,1], 
       [0,3], 
       [4], 
        [1], 
        []]
        0       1     2    3    4   
ans = true

enter room 0
keep track of the keys you have
as you collect keys, jump to the next room that you have a key for
use dfs with stack

[[1,3],[3,0,1],[2],[0]]

Time complexity: O(n.m)
Space complexity: O(n)

'''
# def keysAndRooms(rooms):
#     visited = set()
#     stack=[0]

#     while stack:
#         curRoom=stack.pop() 
#         if curRoom not in visited:
#             visited.add(curRoom) 
#             if rooms[curRoom]:
#                 for key in rooms[curRoom]: 
#                     stack.append(key)
    
#     return len(visited) == len(rooms)

def keysAndRooms(rooms):
    visited = set()

    def dfs(i):
        if i not in visited:
            visited.add(i) 
            if rooms[i]:
                for key in rooms[i]: 
                    dfs(key)
    dfs(0)
    return len(visited) == len(rooms)  
    

def cheq_eq(a,b):
    if a==b:
        print('Test passed')
    else:
        print('Test failed')

print(cheq_eq(keysAndRooms([[1,3],[3,0,1],[2],[0]]), False))
print(cheq_eq(keysAndRooms([[2,1], 
    [0,3], 
       [4], 
        [1], 
        []]), True))
                

    
    
    