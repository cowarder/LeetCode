"""
问题描述：

121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the
stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

"""
解题思路：
迭代数组，每一步求：如果当前价格卖掉股票能够挣多少
记录前面最低价格以及最大利润，利用当前价格减去之前的最低价格，得出当前利润
如果当前利润大于最大利润，更新最大利润
每一步都需要检查是否更新最低价格
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        best_profit = 0
        pre_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - pre_min > best_profit:
                best_profit = prices[i] - pre_min
            pre_min = min(pre_min, prices[i])
        return best_profit