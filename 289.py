"""
问题描述：

289. Game of Life
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight
 neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is
created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells
first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
problems when the active area encroaches the border of the array. How would you address these problems?

"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return board
        m = len(board)
        n = len(board[0])
        new_board = [[None]*n for _ in range(m)]
        def sum_ones(i, j, m, n):
            ones = 0
            if i-1>=0:
                ones += board[i-1][j]
                if j+1<n:
                    ones += board[i-1][j+1]
                if j-1>=0:
                    ones += board[i-1][j-1]
            if j-1 >=0:
                ones += board[i][j-1]
            if j+1<n:
                ones += board[i][j+1]
            if i+1<m:
                ones += board[i+1][j]
                if j-1>=0:
                    ones += board[i+1][j-1]
                if j+1<n:
                    ones += board[i+1][j+1]
            return ones
        for i in range(m):
            for j in range(n):
                ones = sum_ones(i, j, m, n)
                if board[i][j] == 1:
                    if ones <2:
                        new_board[i][j]=0
                    elif ones >3:
                        new_board[i][j]=0
                    else:
                        new_board[i][j]=1
                else:
                    if ones == 3:
                        new_board[i][j]=1
                    else:
                        new_board[i][j]=0
        for i in range(m):
            board[i]=new_board[i]