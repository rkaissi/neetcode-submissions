class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for sC, tC in zip(s, t):
            sMap[sC] = 1 + sMap.get(sC, 0)
            tMap[tC] = 1 + tMap.get(tC, 0)
        
        return sMap == tMap