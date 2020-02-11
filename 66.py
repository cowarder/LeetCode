"""
问题描述：

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        c = 0
        digits[index] += 1
        if digits[index] < 10:
            return digits
        else:
            while index >= 0:
                if digits[index] + c >= 10:
                    digits[index] = (digits[index] + c) % 10
                    c = 1
                    index -= 1
                else:
                    digits[index] = digits[index] + c
                    c = 0
                    break
            if index < 0 and c != 0:
                return [1] + digits
            return digits

a = Solution()
print(a.plusOne([9]))