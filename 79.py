"""

问题描述：
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""

"""
解题思路：DFS
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(word) == 0:
            return False
        self.found = False
        c = word[0]
        m = len(board)
        n = len(board[0])

        def dfs(x, y, index, searched):
            if index == len(word)-1:
                self.found = True
                return
            if self.found == True:
                return
            if x - 1 >= 0 and board[x - 1][y] == word[index + 1] and str(x-1) + "-" + str(y) not in searched:
                dfs(x - 1, y, index + 1, searched | set([str(x-1) + "-" + str(y)]))
            if x + 1 < m and board[x + 1][y] == word[index + 1] and str(x+1) + "-" + str(y) not in searched:
                dfs(x + 1, y, index + 1, searched | set([str(x+1) + "-" + str(y)]))
            if y - 1 >= 0 and board[x][y - 1] == word[index + 1] and str(x) + "-" + str(y-1) not in searched:
                dfs(x, y - 1, index + 1, searched | set([str(x) + "-" + str(y-1)]))
            if y + 1 < n and board[x][y + 1] == word[index + 1] and str(x) + "-" + str(y+1) not in searched:
                dfs(x, y + 1, index + 1, searched | set([str(x) + "-" + str(y+1)]))

        for i in range(m):
            for j in range(n):
                if board[i][j] == c:
                    dfs(i, j, 0, set([str(i)+"-"+str(j)]))
                    if self.found == True:
                        return True
        return self.found

board =[['a','a']
]

word = "aaa"
a = Solution()
print(a.exist(board, word))