"""
问题描述：
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""

"""
解题思路：

利用动态规划的思想，利用一个额外的布尔数组表示直到当前位置的字符串子串是否可以被分解
逐个去与所有的word对比，如果尾部相同并且去掉尾部的头部仍然可以被分解，就是一个合理的分解
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        result = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i-len(word)+1:i+1] == word and (i-len(word) == -1 or result[i-len(word)]):
                    result[i] = True
                    break
        return result[len(s) - 1]

a = Solution()
print(a.wordBreak("cars",["car","ca","rs"]))