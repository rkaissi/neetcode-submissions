class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3

        for num in nums:
            buckets[num] += 1
        
        k = 0
        for i, bucket in enumerate(buckets):
            for j in range(bucket):
                nums[k] = i
                k += 1
