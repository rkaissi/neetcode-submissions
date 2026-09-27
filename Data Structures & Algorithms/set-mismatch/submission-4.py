class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        res = [None, None]
        i = 1
        for num in nums:
            if num in s:
                res[0] = num
            s.add(num)
        
        for i in range(1,n+1):
            if i not in s:
                res[1] = i
                break
        
        return res