"""
问题描述：

75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""

"""
解题思路：
遍历统计所有元素的数目，然后重置数组即可
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for x in nums:
            if x == 0:
                zero += 1
            elif x == 1:
                one += 1
            else:
                two += 1
        nums[:zero] = [0] * len(nums[:zero])
        nums[zero:zero + one] = [1] * len(nums[zero:zero + one])
        nums[(zero + one):(zero + one + two)] = [2] * len(nums[(zero + one):(zero + one + two)])
        return nums


a = Solution()
print(a.sortColors([2,0,2,1,1,0]))