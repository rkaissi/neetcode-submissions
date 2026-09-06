class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        minLen = min(l1, l2)

        for i in range(minLen, 0, -1):
            divisor = str1[:i]
            if l1 % i == 0 and l2 % i == 0:
                concats1 = l1 // i
                concats2 = l2 // i
                s1 = divisor*concats1
                s2 = divisor*concats2

                if s1 == str1 and s2 == str2:
                    return divisor
        
        return ""
