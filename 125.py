"""
问题描述：

125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

"""
解题思路：

alphanumeric指的是数字和字母
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) <= 1:
            return True
        result = []
        for c in s:
            if 0 <= ord(c) - ord('a') <= 26:
                result.append(c)
            elif 0 <= ord(c) - ord('A') <= 26:
                result.append(chr(ord('a') + ord(c) - ord('A')))
            elif 0 <= ord(c) - ord('0') <= 9:
                result.append(chr(ord('0') + ord(c) - ord('0')))
            else:
                continue
        if result == result[::-1]:
            return True
        else:
            False