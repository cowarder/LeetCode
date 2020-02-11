"""
问题描述：

70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""
解题思路：
经典的斐波那契数列的爬楼梯问题：到当前位置x，只能是从x-1和x-2两个台阶跳上来的
所以不断叠加即可
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        n_2 = 1
        n_1 = 2
        for i in range(3, n+1):
            temp = n_2 + n_1
            n_2 = n_1
            n_1 = temp
        return n_1

a = Solution()
print(a.climbStairs(3))