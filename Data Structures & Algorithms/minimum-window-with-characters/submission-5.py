class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        need = len(tMap)
        have = 0
        freqMap = {}
        best = (float("inf"), 0, 0)
        l = 0

        for r, c in enumerate(s):
            if c in tMap:
                freqMap[c] = 1 + freqMap.get(c, 0)
                if freqMap[c] == tMap[c]:
                    have += 1

            while have == need:
                if r - l + 1 < best[0]:
                    best = (r - l + 1, l, r)
                left = s[l]
                if left in tMap:
                    freqMap[left] -= 1
                    if freqMap[left] < tMap[left]:
                        have -= 1
                l += 1

        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]