class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # at each stage maximize current (1-3) and minimize next 3
        n = len(stoneValue)
        dp = [0] * (n+1)
        dp[n] = 0

        for i in range(n-1, -1, -1):
            s = 0
            best = float("-inf")
            for k in range(3):
                if i + k >= n:
                    break
                s += stoneValue[i+k]
                best = max(best, s-dp[i+1+k])
            
            dp[i] = best
        
        print(dp)
        
        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"