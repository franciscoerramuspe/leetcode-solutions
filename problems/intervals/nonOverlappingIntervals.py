'''
Given an array of intervals intervals where intervals[i] = [starti, endi],

return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.


given=[[1,2],[2,3],[3,4],[1,3]]
ans=1


given=[[1,4], [2, 3], [0, 2]]
ans=1

here, we need to be greedy
if we sort the array by the endi (the intervals that end earlier are going to be first)
given=[[1,4], [2, 3], [0, 2]] 
becomes [[0, 2], [2, 3], [1,4]]
and from here, we need an array to keep track of the meetings, and a variable to keep track of the interval end
we will check the each interval, if its starti is >= finish, then add it to the array and update finish
repeat until the end and return len(intervals)-len(ans)

iteration1: 
    finish=2
    ans=[(0, 2)]

iteration2:
    finish=3
    ans=[(0, 2), (2, 3)]
...


Time: O(N)
Space: O(N)
'''
def nonOverlappingIntervals(intervals):
    ans = []
    prevFinish=float('-inf')
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    for i in range(len(sorted_intervals)):
        curIntervalStart=sorted_intervals[i][0]
        if curIntervalStart >= prevFinish:
            ans.append((sorted_intervals[i]))
            prevFinish=sorted_intervals[i][1]
    return len(intervals)-len(ans)

print(nonOverlappingIntervals([[1,4], [2, 3], [0, 2]]) == 1)
print(nonOverlappingIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1)