"""
118. Pascal's Triangle

"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            pre = res[-1]
            temp = [1]
            for i in range(len(res[-1]) - 1):
                temp.append(res[-1][i] + res[-1][i+1])
            temp.append(1)
            res.append(temp)
        return res