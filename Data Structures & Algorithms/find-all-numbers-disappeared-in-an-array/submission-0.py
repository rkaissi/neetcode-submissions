class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums)+1)

        for n in nums:
            arr[n] = 1
        
        res = []
        for i in range(1, len(nums)+1):
            if arr[i] == 0:
                res.append(i)
        
        return res
        