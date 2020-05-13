"""
问题描述：
300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""

"""
解题思路：
问题为求解最长递增子序列长度
动态规划问题，记录前面节点到当前节点的节点数目，当前最长递增子序列数目由之前的节点转移而来

"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums)==1:
            return 1
        m = len(nums)
        dp = [1]*m
        for i in range(m):
            for j in range(i+1, m):
                if nums[i]<nums[j]:
                    dp[j]=max(dp[j], dp[i]+1)
        return max(dp)


a = Solution()
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))