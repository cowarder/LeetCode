"""
问题描述：

49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""

"""
解题思路：


"""
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        split_strs = [" ".join(sorted(x)) for x in strs]
        str_dict = defaultdict(list)
        for i, s in enumerate(split_strs):
            str_dict[s].append(strs[i])
        result = list(str_dict.values())
        return result


a = Solution()
a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])