"""
问题描述：

130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the
board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O'
on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected
horizontally or vertically.

"""

"""
解题思路：
宽度优先搜索，首先找出在边界上面的O字符，然后由此进行宽度优先搜索算法
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return board
        m = len(board)
        n = len(board[0])
        copy = [['X'] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        q = []
        for i in range(m):
            if board[i][0] == 'O':
                q.append([i, 0])
            if board[i][n-1] == 'O':
                q.append([i, n-1])
        for j in range(n):
            if board[0][j] == 'O':
                q.append([0, j])
            if board[m-1][j] == 'O':
                q.append([m-1, j])
        while q:
            x, y = q.pop(0)
            if visited[x][y]:
                continue
            copy[x][y] = 'O'
            visited[x][y] = True
            if x-1 >= 0 and board[x - 1][y] == 'O':
                q.append([x - 1, y])
            if x + 1 < m and board[x + 1][y] == 'O':
                q.append([x + 1, y])
            if y - 1 >= 0 and board[x][y - 1] == 'O':
                q.append([x, y - 1])
            if y + 1 < n and board[x][y+1] == 'O':
                q.append([x, y+1])
        for i in range(m):
            board[i] = copy[i]

board = [['O', 'O'], ['O', 'O']]
a = Solution()
a.solve(board)
print(board)