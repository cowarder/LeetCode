"""
问题描述：

32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""

"""
解题思路：
找到最长的合理括号长度
通过观察发现，如果是一个(或者)是一个合理括号的一部分，那么它一定在制作栈的过程中被pop出来过
我们需要一个新的列表，记录index元素是否被pop出来过，然后利用index找到连续被pop出来元素的连续最大长度
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        poped = [False] * len(s)
        val_stack = []
        index_stack = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                val_stack.append(c)
                index_stack.append(i)
            else:
                if not val_stack:
                    val_stack.append(')')
                    index_stack.append(i)
                elif val_stack[-1] == '(':
                    pre_index = index_stack[-1]
                    poped[pre_index] = True
                    poped[i] = True
                    val_stack = val_stack[:-1]
                    index_stack = index_stack[:-1]
                else:
                    val_stack.append(')')
                    index_stack.append(i)

        result = 0
        i = 0
        while i < len(s):
            if not poped[i]:
                i += 1
                continue
            else:
                j = i
                while j < len(s) and poped[j]:
                    j += 1
                result = max(result, j - i)
                i += 1
        return result

a = Solution()
print(a.longestValidParentheses(')()())'))