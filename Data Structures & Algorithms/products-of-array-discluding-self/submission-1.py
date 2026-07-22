class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            prefix[i] = nums[i] * prefix[max(0, i-1)]
            postfix[len(nums) - i - 1] = nums[len(nums) - i - 1] * postfix[min(len(nums) - 1, len(nums) - i)]
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = postfix[i+1]
            elif i == len(nums) - 1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * postfix[i+1]
        return res