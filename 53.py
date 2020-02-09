"""

问题描述：

53. Maximum Subarray

Given an integer array nums, find the contiguous subarray(containing at least one number) which has
the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer
approach, which is more subtle.
"""

"""
解题思路：

寻找最大连续子串的问题，核心思想是：
记录下来每一步的sum，一旦之前的sum小于0，说明之前的部分对于之后的部分就没有贡献了
sum计算从当前节点重新开始

注释的部分为同时找到和最大对应的子集
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = -float("inf")
        begin = end = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxsum:
                maxsum = sum
                end = i
            if sum < 0:
                sum = 0
        """
        target = nums[end]
        begin = end
        while target != maxsum:
            begin -= 1
            target += nums[begin]
        print(nums[begin:end+1])
        """

        return maxsum


a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))