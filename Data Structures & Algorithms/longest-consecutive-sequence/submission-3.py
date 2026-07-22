class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1 if len(nums) > 0 else 0
        conseq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i-1] + 1:
                conseq += 1
                res = max(conseq, res)
            else:
                conseq = 1
        return res