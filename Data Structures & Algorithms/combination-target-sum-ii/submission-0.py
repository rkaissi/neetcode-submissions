class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, arr, total):
            if total == target:
                res.append(arr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            dfs(i+1, arr+[candidates[i]], total+candidates[i])
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, arr, total)
        
        dfs(0, [], 0)
        return res