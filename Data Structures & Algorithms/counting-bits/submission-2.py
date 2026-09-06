class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        dp[0] = 0
        sigdig = 1

        for i in range(1, n+1):
            if sigdig * 2 == i:
                sigdig *= 2
            dp[i] = 1 + dp[i-sigdig]
        
        return dp