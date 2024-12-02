'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 

You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
new Interval =[7, 10]
given=[[1, 3], 
            [4, 6], 
                     [8,9]], 
                  [7,       10]
return = [[1, 3], [4, 6], [7-10]]
There are two potential cases:
overlap:
    compare first position of newInterval vs last position of each interval
    if numbers are:
    3 6 9

    compare 7 until you find a bigger or equal number
        3 6 9
            7
    add to the ans=min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])
no overlap:
    new Interval =[8, 9]
    given=[[1, 3], 
                [4, 6], 
                              [10, 12]], 
                        [8, 9]

    compare first position of newInterval vs last position of each interval
    if numbers are:
    3 6 12

    compare 7 until you find a bigger or equal number
        3 6 12
            8
    if newInterval[1] < interval[i][0]:
        no overlap, append both to ans
    
Time: O(N) as we go through all the intervals in list
Space:O(N) as we create a new array to return

'''
# [[1,2],[3,5],[6,7],[8,10],[12,16]]  new=[4, 8]
def insertInterval(intervals, newInterval):
   if not intervals:
            return [newInterval]
    ans = []
    startNewInterval=newInterval[0]
    endNewInterval=newInterval[1]
    insertedInterval=False

    for i in range(len(intervals)):
        endCurInterval=intervals[i][1]
        if startNewInterval > endCurInterval:
            ans.append(intervals[i]) # ans = [[1, 3], [4, 6], [7, 10], [11, 13]
            continue
        # check if there is overlap
        # for the largest of number of new (new[1]), check if that number is >= smallest num in cur (cur[0])
        if endNewInterval >= intervals[i][0]: # overlap
            newInterval=[min(startNewInterval, intervals[i][0]), max(endNewInterval, intervals[i][1])]
            startNewInterval=newInterval[0]
            endNewInterval=newInterval[1]
        else: # no overlap
            if not insertedInterval:
                ans.append(newInterval)
                insertedInterval=True
            ans.append(intervals[i])
    if not insertedInterval:
        ans.append(newInterval)
    return ans

print(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))