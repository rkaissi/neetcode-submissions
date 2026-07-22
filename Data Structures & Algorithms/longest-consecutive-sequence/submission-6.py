class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest


        # nums.sort()
        # res = 1 if len(nums) > 0 else 0
        # conseq = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue

        #     if nums[i] == nums[i-1] + 1:
        #         conseq += 1
        #         res = max(conseq, res)
        #     else:
        #         conseq = 1
        # return res