"""
integer array prices
prices[i] is the price of NeetCoin on the ith day

You may choose a single day to buy one NeetCoin
and choose a different day in the future to sell it.

Return the maximum profit you can achieve.
No transactions means 0 -> max(0, profit)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            maxP = max(maxP, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxP