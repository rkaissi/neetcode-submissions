class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, arr, total):
            if total > target or i >= len(nums):
                return

            if total == target:
                res.append(arr.copy())
                return
            
            dfs(i, arr+[nums[i]], total+nums[i])
            dfs(i+1, arr, total)
        
        dfs(0, [], 0)
        return res