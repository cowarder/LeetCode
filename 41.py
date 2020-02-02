"""
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
"""

"""
解题思路：
1 去掉所有小于等于0的数字
2 找到最最小的正整数
3 右最小的正整数递增进行寻找

这里需要注意的一个问题是，如果采用range而不是while循环，第二个参数
设置的过大的化，会出现out of memory的错误
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [x for x in nums if x > 0]
        if len(nums) == 0:
            return 1
        min_value = min(nums)
        if min_value > 1:
            return 1
        else:
            s = set(nums)
            x = min_value
            while x in s:
                x += 1
            return x
        return 0

a = Solution()
print(a.firstMissingPositive([1,2,3,10,2147483647,9]))