class Solution:
    def countBits(self, n: int) -> List[int]:
        def getOnes(dec):
            res = 0
            while dec > 0:
                res += dec % 2
                dec //= 2
            return res
            
        return [getOnes(i) for i in range(n+1)]