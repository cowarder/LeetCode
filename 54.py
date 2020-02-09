"""

问题描述：

54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

"""
解题思路：
可以想像成一个小狗，碰头就往右转，直到无路可走，这里的无路可走我们采用一个与输入数组大小相同的数组表示
其中的元素表示此元素是否被访问过
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        searched = [[False] * n for _ in range(m)]
        result = []
        i = j = 0
        searched_num = 0
        target_num = m * n
        while searched_num != target_num:
            while j < n and not searched[i][j]:
                result.append(matrix[i][j])
                searched[i][j] = True
                searched_num += 1
                j += 1
            j -= 1
            i += 1
            while i < m and not searched[i][j]:
                result.append(matrix[i][j])
                searched[i][j] = True
                searched_num += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and not searched[i][j]:
                result.append(matrix[i][j])
                searched[i][j] = True
                searched_num += 1
                j -= 1
            j += 1
            i -= 1
            while i > 0 and not searched[i][j]:
                result.append(matrix[i][j])
                searched[i][j] = True
                searched_num += 1
                i -= 1
            i += 1
            j += 1
        return result

m = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
a = Solution()
a.spiralOrder(m)