class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # return nums * 2
        res = [0] * len(nums) * 2
        for i, n in enumerate(nums):
            res[i] = res[i + len(nums)] = n
        return res