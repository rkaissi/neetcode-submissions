class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = []

        curSum = 0
        for n in nums:
            self.prefixSum.append(curSum)
            curSum += n
        self.prefixSum.append(curSum)
        print(self.prefixSum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)