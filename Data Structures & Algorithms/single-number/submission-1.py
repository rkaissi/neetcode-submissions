class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hs = set()

        for n in nums:
            if n in hs:
                hs.remove(n)
            else:
                hs.add(n)
            
        return list(hs).pop()