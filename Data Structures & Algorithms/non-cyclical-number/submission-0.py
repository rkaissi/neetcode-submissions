class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def getDigits(num):
            digits = []
            for c in str(num):
                digits.append(int(c))
            return digits
        
        while n != 1:
            n = sum([digit*digit for digit in getDigits(n)])
            if n in seen:
                return False
            seen.add(n)
        
        return True