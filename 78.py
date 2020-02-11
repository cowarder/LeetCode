"""

问题描述：

78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

"""
解题思路：BFS
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def dfs(index, path):
            result.append(path)
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])
        dfs(0, [])
        return result


a = Solution()
print(a.subsets([1,2,3]))