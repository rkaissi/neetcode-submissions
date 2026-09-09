class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sumOfSquares(num):
            s = 0
            while num > 0:
                d = num % 10
                s += d*d
                num //= 10
            return s
        
        while n != 1:
            n = sumOfSquares(n)
            if n in seen:
                return False
            seen.add(n)
        
        return True