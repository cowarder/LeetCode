"""
问题描述：

33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


"""
解题思路

1 需要将几个pivot的位置找出来，找出来每个区间的起始、终止位置，以及起始位置的值
2 利用(起始位置，终止位置，起始位置的值)构建新的有序数组
3 在有序数组中利用二分查找找到对应的索引值
4 将值对应会原来的数组的索引
"""


def binary_search(list_item,item):
    low = 0
    high = len(list_item)
    while low < high:
        mid = int((low + high)/2)
        guess = list_item[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid
        else:
            low = mid + 1
    return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index_dict = dict(zip(nums, range(len(nums))))
        if len(nums) == 0:
            return -1
        pivots = []
        begin = end = 0
        while end < len(nums) - 1:
            end += 1
            if nums[end] >= nums[end-1]:
                continue
            else:
                pivots.append((begin, end, nums[begin]))
                begin = end
        pivots.append((begin, end + 1, nums[begin]))
        pivots = sorted(pivots, key=lambda x:x[2])
        new_nums = []
        for p in pivots:
            new_nums += nums[p[0]:p[1]]
        new_index = binary_search(new_nums, target)
        if new_index != -1:
            num = new_nums[new_index]
            return index_dict[num]
        return -1


a = Solution()
print(a.search([4,5,6,7,0,1,2], 0))