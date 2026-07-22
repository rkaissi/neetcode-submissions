class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] <= nums[r]:
                r = m
            else:
                l = m + 1
        
        startOfSecond = l
        if target <= nums[-1]:
            return self.binSearch(nums, startOfSecond, len(nums) - 1, target)
        else:
            return self.binSearch(nums, 0, startOfSecond - 1, target)

    def binSearch(self, nums, l, r, target):
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1
