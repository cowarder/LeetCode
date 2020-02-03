"""
问题描述：

39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""

"""
解题思路：
利用深度优先搜索算法进行搜索
这里需要注意的是每个数字可以无限重复利用，所以下一次dfs的时候需要从当前索引开始回溯
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(remain, index, path):
            if remain < 0:
                return
            if remain == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(remain-candidates[i], i, path+[candidates[i]])
        dfs(target, 0, [])
        # for x in result:
        #     print(x)
        return result


a = Solution()
a.combinationSum([2,3,5], 8)