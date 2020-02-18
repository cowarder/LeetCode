"""

122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
 (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

"""

"""
解题思路：
利用贪心策略，从最低点出发，在价格最低的时候买进，在价格没有出现下降的时候卖出
然后在找后面的最低点买进，最高点卖出

例如：8，7，6，5，4，6，8，10，12
在前面的最低点4买进，在最高点12卖出，在4和12之间无论如何买进卖出，利润都不会超过12-4
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        result = 0
        buy = sell = 0
        while buy < len(prices) and sell < len(prices):
            while buy < len(prices) - 1 and prices[buy] >= prices[buy + 1]:
                buy += 1
            sell = buy + 1
            if sell >= len(prices):
                break
            while sell < len(prices) and prices[sell] > prices[sell - 1]:
                sell += 1
            if sell < len(prices):
                result += prices[sell - 1] - prices[buy]
                buy = sell
                sell = buy
            else:
                result += prices[len(prices) - 1] - prices[buy]
        return result
