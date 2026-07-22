class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in s:
            if (n - 1) in s:
                continue
            k = 0
            j = n
            while j in s:
                k += 1
                j += 1
            res = max(res, k)
        return res