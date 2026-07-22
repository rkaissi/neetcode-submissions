class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreqMap = {}
        tFreqMap = {}

        for c in s:
            sFreqMap[c] = 1 + sFreqMap.get(c, 0)
        for c in t:
            tFreqMap[c] = 1 + tFreqMap.get(c, 0)
        
        return sFreqMap == tFreqMap