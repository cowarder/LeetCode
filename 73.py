"""
问题描述：

73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""

"""
解题思路：
采用O(m+n)的空间复杂度，另外一种改进策略是利用数组的第一行和第一列来存储是否为0
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        zero_col = set()
        zero_row = set()
        if len(matrix) == 0:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        for row in range(m):
            if row in zero_row:
                matrix[row] = [0] * n
                continue
            else:
                for col in zero_col:
                    matrix[row][col] = 0
        return matrix


m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
a = Solution()
a.setZeroes(m)