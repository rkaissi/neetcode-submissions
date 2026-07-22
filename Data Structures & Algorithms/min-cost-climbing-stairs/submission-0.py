class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dfs(i):
            if i >= n:
                return 0
            
            one = cost[i] + dfs(i+1)
            two = cost[i] + dfs(i+2)

            return min(one, two)
        
        return min(dfs(0), dfs(1))