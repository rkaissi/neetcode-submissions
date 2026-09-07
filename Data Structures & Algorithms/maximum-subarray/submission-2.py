class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        runningSum = 0
        for n in nums:
            if runningSum < 0:
                runningSum = 0
            runningSum += n
            res = max(res, runningSum)
        
        return res