"""
问题描述：
42. Trapping Rain Water


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute
how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""


"""
解题思路：
两指针问题
1 分别用两个指针表示左右两边的隔板高度
2 找到两个指针中高度相对较低的指针a
3 由a开始出发，向另外一个指针方向移动，累加高度
4 直到找到一个比a高度高的隔板，跳转到2
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        while l < r and height[l] <= height[l+1]:
            l += 1
        while l < r and height[r] <= height[r-1]:
            r -= 1
        result = 0
        while l < r:
            left = height[l]
            right = height[r]
            if left <= right:
                l += 1
                while l < r and left >= height[l]:
                    result += left - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and right >= height[r]:
                    result += right - height[r]
                    r -= 1
        return result

a = Solution()
print(a.trap([2, 0, 2]))