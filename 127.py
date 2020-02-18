"""

问题描述：

127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

"""

"""
解题思路：
利用宽度优先搜索的方法，首先求出当前字符串下一个变化状态，称为他的neighbor，然后从neighbor出发，继续寻找neighbor

这里不一样的是，求出每个字符串的下个状态是否存在待比较的集合里面，然后需要将对应的值从待比较集合里面剔除
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        begin = set([beginWord])
        end = set(wordList)
        depth = 0
        while len(begin) != 0:
            temp = set()
            for word in begin:
                if word == endWord:
                    return depth + 1
                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                        if new_word in end:
                            temp.add(new_word)
                            end.remove(new_word)
            begin = temp
            depth += 1
        return 0

