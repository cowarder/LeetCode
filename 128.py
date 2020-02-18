"""
问题描述：

128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""

"""
解题思路：
利用哈希解决，当前位置记录从当前位置到最前方（包括当前位置）的连续最大长度，当前位置之后的最大连续长度都需要加上当前位置的长度值
"""

from collections import defaultdict


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        m = defaultdict(int)
        max_len = 1
        for num in nums:
            if num in m:
                continue
            add = 0
            if num - 1 in m:
                m[num] = m[num-1] + 1
            else:
                m[num] = 1
            upper = num + 1
            while upper in m:
                m[upper] += m[num]
                upper += 1
            max_len = max(max_len, m[upper-1])
            # print(m)
        if max_len == 1:
            return 1
        else:
            return max_len
a = Solution()

print(a.longestConsecutive([100,4,200,1,3,2]))