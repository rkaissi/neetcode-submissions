from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = {}, {}

        if len(s) != len(t):
            return False
        
        for sChar, tChar in zip(s, t):
            sCount[sChar] = 1 + sCount.get(sChar, 0)
            tCount[tChar] = 1 + tCount.get(tChar, 0)
        
        return sCount == tCount