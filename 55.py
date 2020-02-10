"""
问题描述：
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""

"""
解题思路：
一开始想的是利用DFS的思路来解，但是只通过了70/75个测试用例，原因是时间复杂度太高了
后面采用了一种O(n)的思路：
    遍历所有数组，走到每一步的时候记录当前位置能够到达的最远路径，再走到下一步
    如果走到下一步，发现之前的最远到达不了这里，那就意味着路径是中断的，也就不可能到达最终目的地
"""

"""
改进策略，如果要求出所有可能的路径的话，就需要采用DFS的思路
如果仅仅需要求出一条路径
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True

        """
        # dfs version 70/75 passed
        result = []
        def dfs(index, path):
            if index == len(nums) - 1:
                result.append(path)
                return
            elif index >= len(nums):
                return
            for i in range(1, nums[index] + 1):
                dfs(index+i, path + [i])
        dfs(0, [])
        if len(result) != 0:
            return True
        else:
            return False
        """


a = Solution()
print(a.canJump([3,2,1,0,4]))