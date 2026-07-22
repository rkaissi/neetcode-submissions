class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += f"{len(s)}#{s}"
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            sLen = ""
            while s[i] != "#":
                sLen += s[i]
                i += 1
            
            sLen = int(sLen)
            j = i + 1 # Skip the #
            nextIdx = j+sLen
            res.append(s[j:nextIdx])
            i = nextIdx
        
        return res
