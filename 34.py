"""
问题描述：

34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""


"""
解题思路

1. 二分查找找出对应的索引
2. 由索引向左向右找出相同值的最左最右索引
"""


def binary_search(array, target):
    low = 0
    high = len(array)
    while low < high:
        mid = (low + high) // 2
        value = array[mid]
        if value == target:
            return mid
        if value > target:
            high = mid
        else:
            low = mid + 1
    return -1


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = binary_search(nums, target)
        if index == -1:
            return [-1, -1]
        left = right = index
        while left >= 0 and nums[left] == target:
            left -= 1
        left += 1
        while right < len(nums) and nums[right] == target:
            right += 1
        right -= 1
        return [left, right]

a = Solution()
print(a.searchRange([2,2], 2))
