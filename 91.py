"""

问题描述描述：
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""

"""
解题思路：
问题思路很简单，总体是当前字符可以从前一个字符得来，或者与前一个字符共同构成一个字符，这样的话，到达当前
位置n的路径数目num(n)是num(n-1)和num(n-1)的和，但是这个问题隐含了许多边界条件，很难考虑周到

1. 首先是获取前两个值的时候，需要注意10和20只有一种组成可能性，以及如果第二个数字为0，第一个不能大于2
2. 循环迭代过程中，如果两个0相连或者0前面的数组大于2都是不合理的，如00或者505
3. 当前字符为0，只能与前面的字符构成一个整体，需要回退，way_s=way_f
4. 当前字符不为0，但是前面的字符为0或者跟前面字符构成的数字大于26，那就说明前面两个字符构成整体
5. 最后一种情况就是num(n) = num(n-1) + num(n-1)
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if ord(s[0]) - ord('0') == 0:
            return 0
        elif len(s) == 1:
            return 1
        f_c = ord(s[0]) - ord('0')
        s_c = ord(s[1]) - ord('0')
        pre_c = s_c
        way_f = 1
        if s_c == 0 and f_c > 2:
            return 0
        elif 1 < (f_c * 10 + s_c) <= 26 and (f_c * 10 + s_c) != 20 and (f_c * 10 + s_c) != 10:
            way_s = 2
        else:
            way_s = 1
        for i in range(2, len(s)):
            c = ord(s[i]) - ord('0')
            # print(way_f, way_s)
            print(c, pre_c)
            if c == pre_c == 0 or (c == 0 and pre_c > 2):
                return 0
            if c == 0:
                way_s = way_f
            elif pre_c == 0 or pre_c * 10 + c > 26:
                way_f = way_s
            else:
                temp = way_s + way_f
                way_f = way_s
                way_s = temp
            pre_c = ord(s[i]) - ord('0')
        return way_s


a = Solution()
print(a.numDecodings("302"))