'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.

The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

deadends=['0004', '1234', '7943', '5566']
target='5565'

try all possible combinations with bfs until you find the target.
keep track of how many moves it takes you to reach to each new number
once you find the target return number of moves

'''
def openLock(deadends, target):
    if '0000' in deadends:
        return -1
    
    def getNewPositions(lock):
        res =[]
        for i in range(4):
            digit =str((int(lock[i]) + 1) %10)
            res.append(lock[:i] + digit + lock[i+1:]) # adding one to the current lock stat
            digit =str((int(lock[i]) - 1 + 10) %10)
            res.append(lock[:i] + digit + lock[i+1:]) # deleting one to the current lock stat
        return res


    queue=deque() # will store which combination I am at and at what cost I got there
    queue.append(['0000', 0])
    visited = set(deadends) # we initialize the deadends as part of visited to avoid getting there
    
    while queue:
        lockPosition, cost = queue.popleft()
        if lockPosition == target:
            return cost
        for newPos in getNewPositions(lockPosition):
            if newPos not in visited:
                visited.add(newPos)
                queue.append([newPos, cost+1])
    return -1
