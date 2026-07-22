class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += f"{len(s)}#{s}"
        
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        i, j = 0, 0
        nextStrLen = 0
        while i < len(s):
            if s[i] == "#":
                nextStrLen = int(s[j:i])
                i += 1
                output.append(s[i: i + nextStrLen])
                i += nextStrLen
                j = i
            else:
                i += 1
        
        return output