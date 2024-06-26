# 57. Insert Interval
# Medium
# Topics
# Companies
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []

    # we want to range over the index here so we can use the index to slice, we could probably also enumerate
    for i in range(len(intervals)):
        # iterate through ad append to res
        # IF we find where the new Interval should go append it to the res or merge
        # continue until we run out of intervals to append

        # if the max of the new interval is less than the start of the next interval we can append the new interval
        # + rest of the intervals into the result
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            res = res + intervals[i:]
            return res
        # if the start of the new interval is greater than the end of the current interval being ranged
        # over append the current interval
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    res.append(newInterval)

    return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

print(insert(intervals, newInterval))

# solution using enumerate
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []
#
#         # we want to range over the index here so we can use the index to slice, we could probably also enumerate
#         for i, inter in enumerate(intervals):
#             # iterate through ad append to res
#             # IF we find where the new Interval should go append it to the res or merge
#             # continue until we run out of intervals to append
#             start, end = inter
#             start_new_inter, end_new_inter = newInterval
#             # if the max of the new interval is less than the start of the next interval we can append the new interval
#             # + rest of the intervals into the result
#             if end_new_inter < start:
#                 res.append(newInterval)
#                 res = res + intervals[i:]
#                 return res
#             # if the start of the new interval is greater than the end of the current interval being ranged
#             # over append the current interval
#             elif start_new_inter > end:
#                 res.append(inter)
#             else:
#                 newInterval = [min(newInterval[0], inter[0]), max(newInterval[1], inter[1])]
#
#         res.append(newInterval)
#
#         return res
