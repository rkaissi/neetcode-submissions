class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        product = 1
        res = 0

        while r < len(nums):
            product *= nums[r]
            while product >= k and l <= r:
                product //= nums[l]
                l += 1
            
            res += r-l+1
            r += 1
        
        return res
            

            
            