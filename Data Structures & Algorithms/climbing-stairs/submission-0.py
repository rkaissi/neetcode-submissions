class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n < 0:
            return 0
        
        one = self.climbStairs(n - 1)
        two = self.climbStairs(n - 2)

        return one + two