class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[i] != "#" and i < len(s):
                i += 1
            sLen = int(s[j:i])
            res.append(s[i+1:i+sLen+1])
            i = j = i + sLen + 1
        
        return res