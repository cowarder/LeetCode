"""
问题描述：
209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""

"""
解题思路：

求出数列中，连续和大于等于s的最短序列长度
考虑到数组中的连续问题，应该想到双指针
这里我们用两个指针left和right来表示求和数组的两端，当两端之间的和大于等于s的时候
需要将左边的指针右移，直到两个指针之间的和小于s
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        l = r = 0
        min_num = float("inf")
        tmp_sum = 0
        while r < len(nums):
            tmp_sum += nums[r]
            r += 1
            while tmp_sum >= s:
                tmp_sum -= nums[l]
                min_num = min(min_num, r-l)
                l += 1
        if min_num == float('inf'):
            return 0
        else:
            return min_num