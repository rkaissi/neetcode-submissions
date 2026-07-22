class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m
        
        l1, r1 = 0, max(0, l - 1)
        l2, r2 = l, len(nums) - 1
        l, r = 0, 0

        print(l1, r1)
        print(l2, r2)

        if target >= nums[l1] and target <= nums[r1]:
            l, r = l1, r1
        else:
            l, r = l2, r2
        
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1