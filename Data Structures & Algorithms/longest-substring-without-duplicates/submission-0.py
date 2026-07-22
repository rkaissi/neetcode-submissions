class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        charset = set()
        maxLen = 0

        while right < len(s):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            right += 1
            maxLen = max(maxLen, right - left)
        return maxLen