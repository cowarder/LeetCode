"""
问题描述：

36. Valid Sudoku

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""

"""
解题思路：
利用一个字典表示字符是否出现过
分别对行、列、3x3方块进行判断
"""

import numpy as np


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rep_dict = {}
        board = np.array(board)
        for row in board:
            for c in row:
                if c == '.':
                    continue
                elif c in rep_dict:
                    return False
                else:
                    rep_dict[c] = 1
            rep_dict = {}
        rep_dict = {}
        for i in range(len(board[0])):
            col = board[:, i]   # col = [col[i] for col in board]
            for c in col:
                if c == '.':
                    continue
                elif c in rep_dict:
                    return False
                else:
                    rep_dict[c] = 1
            rep_dict = {}
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                rep_dict = {}
                for x in range(3):
                    for y in range(3):
                        c = board[row + x][col + y]
                        if c == '.':
                            continue
                        elif c in rep_dict:
                            return False
                        else:
                            rep_dict[c] = 1
                rep_dict = {}

        return True


v = [[".",".","4",".",".",".","6","3","."],
     [".",".",".",".",".",".",".",".","."],
     ["5",".",".",".",".",".",".","9","."],
     [".",".",".","5","6",".",".",".","."],
     ["4",".","3",".",".",".",".",".","1"],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".","5",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]
a = Solution()
print(a.isValidSudoku(v))