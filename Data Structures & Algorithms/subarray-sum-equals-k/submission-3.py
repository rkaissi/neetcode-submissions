class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        curSum = 0
        res = 0
        for i, n in enumerate(nums):
            res += hashmap.get(curSum - k, 0)
            hashmap[curSum] = 1 + hashmap.get(curSum, 0)
            curSum += n
        res += hashmap.get(curSum - k, 0)

        return res