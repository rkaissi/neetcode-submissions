class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return 1
            
            res = 0
            for i in range(len(nums)):
                if n - nums[i] >= 0:
                    res += solve(n - nums[i])
            
            memo[n] = res
            return res

        return solve(target)