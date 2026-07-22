from collections import deque
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Modifies the array
        # for i in range(len(nums)):
        #     if nums[abs(nums[i])] < 0:
        #         return abs(nums[i])
        #     nums[abs(nums[i])] *= -1

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow