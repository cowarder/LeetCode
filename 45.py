"""
问题描述：

45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

"""

"""
解题思路：
开始想的是，求出到每一个位置最短路径长度，然后取最后一个位置元素的值
但是这样只通过了90/92个测试用例，因为其中的数很大，数量很多，时间超出
论坛上面有神仙解法：（愣是没看懂，留待后续）

public int jump(int[] A) {
    int jumps = 0, curEnd = 0, curFarthest = 0;
    for (int i = 0; i < A.length - 1; i++) {
        curFarthest = Math.max(curFarthest, i + A[i]);
        if (i == curEnd) {
            jumps++;
            curEnd = curFarthest;
        }
    }
    return jumps;
}

"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 1
        reachable = [float("inf")] * len(nums)
        reachable[0] = 0
        index = 0
        while index < len(nums):
            for i in range(1, nums[index]+1):
                if index + i >= len(nums):
                    break
                reachable[index + i] = min(reachable[index] + 1, reachable[index + i])
            index += 1
        return reachable[len(nums) - 1]


a = Solution()
print(a.jump([2,3,1,1,4]))