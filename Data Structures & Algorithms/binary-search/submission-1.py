class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            median = (left + right) // 2

            if target == nums[median]:
                return median
            if target < nums[median]:
                right = median - 1
            else:
                left = median + 1
        
        return -1