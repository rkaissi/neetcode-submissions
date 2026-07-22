class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if nums[abs(n)] < 0:
                nums[abs(n)] = 0
            else:
                nums[abs(n)] *= -1
        
        print(nums)
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return i
        