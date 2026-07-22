class Solution:
    def rob(self, nums: List[int]) -> int:
        # BOTTOM UP
        one, two = 0, 0

        for n in nums:
            temp = max(n + one, two)
            one = two
            two = temp
        
        return two

        
        # TOP DOWN
        # n = len(nums)
        # cache = {}
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if i in cache:
        #         return cache[i]

        #     take = nums[i] + dfs(i + 2)
        #     skip = dfs(i + 1)

        #     cache[i] = max(take, skip)
        #     return cache[i]
        
        # return dfs(0)