"""
问题描述：

40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

"""

"""
解题思路：
类似39题，区别就是有重复，且每个只能使用一次，利用深度优先搜索算法进行搜索
如果同一个数字不能够重复的话，下一个的索引应该为i+1
同时这里会有一个重复的问题，比如(1，2，2，3)会出现两个(1，2，3)的情况
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        # candidates = sorted(candidates)

        def dfs(remain, index, path):
            if remain < 0:
                return
            if remain == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(remain-candidates[i], i+1, path+[candidates[i]])
        dfs(target, 0, [])
        for x in result:
             print(x)
        return result


a = Solution()
a.combinationSum2([2, 5, 2, 1, 2], 5)