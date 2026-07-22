from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sSet, tSet = {}, {}

        for sC, tC in zip(s, t):
            sSet[sC] = 1 + sSet.get(sC, 0)
            tSet[tC] = 1 + tSet.get(tC, 0)

        return sSet == tSet