class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def backtrack(i, arr):
            if i >= n:
                res.append(arr[:])
                return

            arr.append(nums[i])
            backtrack(i+1, arr)
            arr.pop()

            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1, arr)
        
        backtrack(0, [])
        return res