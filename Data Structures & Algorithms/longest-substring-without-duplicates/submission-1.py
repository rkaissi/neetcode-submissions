class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        subset = set()
        maxLen = 0

        while r < len(s):
            if s[r] not in subset:
                subset.add(s[r])
                r += 1
                maxLen = max(maxLen, r - l)
                continue
            
            while s[r] in subset:
                subset.remove(s[l])
                l += 1
        
        return maxLen