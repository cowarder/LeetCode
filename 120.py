"""
问题描述：

120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""

"""
解题思路：
利用动态规划的思想，当前状态array[i][j]来自于array[i-1][j]和array[i-1][j-1]

"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return None
        min_sum = [[None] * (i+1) for i in range(len(triangle))]
        min_sum[0][0]=triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    min_sum[i][j]=min_sum[i-1][j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    min_sum[i][j]=min_sum[i-1][j-1]+triangle[i][j]
                else:
                    min_sum[i][j]=min(min_sum[i-1][j-1], min_sum[i-1][j])+triangle[i][j]
        return min(min_sum[len(triangle)-1])


# 优化1：只用一个数组来表示上一层的最小和
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return None
        min_sum=[triangle[0][0]]
        for i in range(1,len(triangle)):
            cur_sum = [None]*len(triangle[i])
            for j in range(len(triangle[i])):
                if j==0:
                    cur_sum[j]=min_sum[j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    cur_sum[j]=min_sum[j-1]+triangle[i][j]
                else:
                    cur_sum[j]=min(min_sum[j-1], min_sum[j])+triangle[i][j]
            min_sum = cur_sum
        return min(min_sum)