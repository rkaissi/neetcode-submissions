from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_set, t_set = defaultdict(int), defaultdict(int)
        
        for sc, tc in zip(s, t):
            s_set[sc] += 1
            t_set[tc] += 1
        return s_set == t_set