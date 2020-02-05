"""
问题描述：

46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

"""
解题思路：
利用dfs思想，每次从数组中取出来一个元素，剩下的所有元素构成一个新的数组，继续进行回溯
每次需要记录当前路径
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(nums, path):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        dfs(nums, [])
        for x in result:
            print(x)
        return result


a = Solution()
a.permute([1, 2, 3])