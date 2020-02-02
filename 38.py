"""
问题描述：

38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

"""

"""
解题思路：

"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        li = ['1', '11', '21', '1211', '111221']
        string = li[4]
        for index in range(5, 30):
            result = ""
            begin = end = 0
            while begin<len(string) and end < len(string):
                c = string[begin]
                while end<len(string) and string[begin] == string[end]:
                    end += 1
                num = end - begin
                begin = end
                result += str(num)
                result += c
            string = result
            li.append(result)
        return li[n-1]

a = Solution()
print(a.countAndSay(2))