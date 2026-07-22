class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        m1 = {}
        
        for c in s1:
            m1[c] = 1 + m1.get(c, 0)

        while r <= len(s2):
            m2 = {}
            for i in range(l, r):
                c = s2[i]
                m2[c] = 1 + m2.get(c, 0)
            if m1 == m2:
                return True
            l += 1
            r += 1
        return False
            
