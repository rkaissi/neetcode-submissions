class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        for i in range(len(first), 0, -1):
            prefix = first[:i]
            common = True
            for j in range(1, len(strs)):
                if strs[j][:i] != prefix:
                    common = False
                    break
            if common: return prefix
        return ""