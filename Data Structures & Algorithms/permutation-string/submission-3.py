from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Map = defaultdict(int)

        for c in s1:
            s1Map[c] += 1
    
        l, r = 0, len(s1) - 1
        subMap = defaultdict(int)

        for i in range(r+1):
            subMap[s2[i]] += 1

        while r < len(s2):
            if subMap == s1Map:
                return True
            
            subMap[s2[l]] -= 1
            if subMap[s2[l]] == 0:
                del subMap[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                subMap[s2[r]] += 1
    
        return False