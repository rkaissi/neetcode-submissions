class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqMap = {}

        for c in s:
            freqMap[c] = 1 + freqMap.get(c, 0)

        res = 0
        oddExists = False

        for v in freqMap.values():
            if v % 2 == 0:
                res += v
            else:
                res += (v-1) if v >= 3 else 0
                oddExists = True
        
        res += 1 if oddExists else 0
        return res
            
        