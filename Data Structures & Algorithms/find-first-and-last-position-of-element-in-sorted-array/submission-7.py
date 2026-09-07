class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m
        
        left = l

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2

            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1

        right = r

        if nums[left] != target:
            return [-1, -1]

        return [left, right]