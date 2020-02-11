"""
问题描述：
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

"""

"""
解题思路：
一道动态规划的问题，到位置(i,j)的可能路线数目为到位置(i-1, j)，(i, j-1)的路线数目的和
更新方程:dp[i][j] = dp[i-1][j] + dp[i][j-1]
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp[m-1][n-1])
        return dp[m-1][n-1]

        """
        result = []
        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                self.paths += 1
                return
            if x < m - 1:
                dfs(x+1, y)
            if y < n - 1:
                dfs(x, y + 1)
        self.paths = 0
        dfs(0, 0)
        return self.paths
        """


a = Solution()
a.uniquePaths(3, 3)