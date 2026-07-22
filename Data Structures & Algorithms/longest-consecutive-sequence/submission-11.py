class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)

        for n in nums:
            if (n - 1) not in numSet:
                i = 0
                while (n + i) in numSet:
                    i += 1
                maxLen = max(maxLen, i)
        
        return maxLen