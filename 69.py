"""
题目描述：

69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

"""

"""
按照常规思路来的，首先以10为量级1，10，100，1000...首先判断数字位于哪个区间
然后对这个区间进行二分查找
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_value = 1
        while max_value*max_value <= x:
            max_value *= 10
        min_value = max_value // 10
        while max_value - min_value > 1:
            mid = (min_value + max_value) // 2
            if mid * mid == x:
                return mid
            if mid*mid > x:
                max_value = mid
            else:
                min_value = mid
        return min_value

a = Solution()
print(a.mySqrt(100))