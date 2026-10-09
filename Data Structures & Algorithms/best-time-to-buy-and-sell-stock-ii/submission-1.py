class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, sell, nothing
        n = len(prices)
        memo = {}

        def dp(i: int, holding: bool):
            if i == n:
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]

            skip = dp(i+1, holding)
            sell = (prices[i] + dp(i+1, False)) if holding else 0
            buy = (dp(i+1, True) - prices[i]) if not holding else 0

            memo[(i, holding)] = max(buy, sell, skip)
            return memo[(i, holding)]
        
        return dp(0, False)

        # buy, profit => 1, -7
        # sell, profit => 0, 7
        # nothing, profit => 