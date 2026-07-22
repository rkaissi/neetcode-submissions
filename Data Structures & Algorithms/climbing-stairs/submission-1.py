class Solution:
    def climbStairs(self, n: int) -> int:
        # BOTTOM UP
        one, two = 1, 1

        for i in range(n-1):
            one, two = two, one + two

        return two

        # TOP DOWN
        # cache = {}
        # def dfs(i):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     if i in cache:
        #         return cache[i]
            
        #     cache[i] = dfs(i+1) + dfs(i+2)
        #     return cache[i]
        
        # return dfs(0)