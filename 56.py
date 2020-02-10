"""

问题描述：

56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get
new method signature.
"""

"""
解题思路：
首先根据每一个区间的起始位置由小到大进行排序，如果后面的begin小于等于前面的end，两者就可以合并
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        begin, end = intervals[0]
        result = []
        for b, e in intervals[1:]:
            if b <= end:
                end = max(e, end)
            else:
                result.append([begin, end])
                begin = b
                end = e
        result.append([begin, end])
        return result


a = Solution()
a.merge([[1,1],[1,1]])
