class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j, l = i+1, len(nums) - 1
            while j < l:
                s = nums[i] + nums[j] + nums[l]

                if s > 0:
                    l -= 1
                elif s < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[l]])
                    j += 1
                    while j < l and nums[j] == nums[j-1]:
                        j += 1

        return res