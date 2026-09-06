class Solution:
    def countBits(self, n: int) -> List[int]:
        def getOnes(dec):
            res = 0
            while dec > 0:
                res += dec & 1
                dec >>= 1
            return res
            
        return [getOnes(i) for i in range(n+1)]