class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        allSubsets = []
        for i in range(0, 1 << n):
            curSubset = []
            for j in range(n):
                if (i >> j) & 1:
                    curSubset.append(nums[j])
            allSubsets.append(curSubset)
        return allSubsets
