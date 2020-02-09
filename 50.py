"""

问题描述：

50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""

"""
解题思路：
采用了递归的思想解决，这里需要注意的问题是n的取值范围，如果采用直观思路，通过
迭代来进行运算的话，由于n的取值范围太大，势必会造成Time Limit Error
"""


class Solution(object):
    def myPow(self, x, n):

        def getPow(x_m, n_m):
            if n_m < 0:
                return 1 / getPow(x_m, -n_m)
            if n_m == 0:
                return 1
            if n_m % 2 == 1:
                return x_m * getPow(x_m*x_m, n_m // 2)
            else:
                return getPow(x_m*x_m, n_m // 2)
        return getPow(x, n)


a = Solution()
print(a.myPow(2, -2))