class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for n in numSet:
            j = n+1
            curLen = 1
            while j in numSet:
                curLen += 1
                j += 1
            maxLen = max(maxLen, curLen)
        
        return maxLen