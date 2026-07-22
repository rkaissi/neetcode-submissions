class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = []
        t_chars = []

        for char in s:
            s_chars.append(char)
        for char in t:
            t_chars.append(char)
        s_chars.sort()
        t_chars.sort()
        return s_chars == t_chars