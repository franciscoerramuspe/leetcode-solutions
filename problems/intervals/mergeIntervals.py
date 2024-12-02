'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

given =[[1,4], [3, 6], [5, 10]]
return = [[1,10]]

if we compare two intervals at a time, we would take the endpoint of the first interval, and compare it to the starting point of the next interval
if intervals[i-1][1] >= intervals[i][0]:
    newInterval=[intervals[i-1][0], intervals[i][1]]
else:
    keep the same interval

repeat until the end of the intervals array

given=[[1,3], [4, 6], [6, 8]]
return=[[1,3], [4, 8]]

Time: O(nlgn) as we have to sort the array
Space: O(n) as we will create an extra list to return
'''
def mergeIntervals(intervals):
    ans = []
    if len(intervals)==1:
        return [intervals[0]]
    intervals.sort()
    prevInterval=intervals[0]
    for i in range(1, len(intervals)):
        if ans:
            prevInterval=ans[-1]
        curInterval=intervals[i]
        if prevInterval[1] >= curInterval[0]:
            if ans:
                ans.pop()
            ans.append([min(prevInterval[0], curInterval[0]), max(curInterval[1], prevInterval[1])])
        else:
            if not ans:
                ans.append(prevInterval)
            ans.append(curInterval)
    return ans

print(mergeIntervals([[1,3], [4, 6], [6, 8]]))
print(mergeIntervals([[1, 4], [0, 4]]))
print(mergeIntervals([[1, 4], [2, 3]]))