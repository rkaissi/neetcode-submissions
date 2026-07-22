class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            preProduct[i] = product
            product *= nums[i]
        
        postProduct = [1] * len(nums)

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            postProduct[i] = product
            product *= nums[i]
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = preProduct[i] * postProduct[i]
        
        return res