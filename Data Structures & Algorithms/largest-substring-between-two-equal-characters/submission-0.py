class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        res = -1

        for i, c in enumerate(s):
            if c in first:
                res = max(res, i-first[c]-1)
            else:
                first[c] = i
        
        return res