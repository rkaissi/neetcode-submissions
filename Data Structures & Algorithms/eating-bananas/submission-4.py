class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min eating speed = 1
        # max eating speed = max(piles)
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2

            t = 0
            for p in piles:
                t += math.ceil(p / m)
            
            if t <= h:
                r = m
            else:
                l = m + 1
        
        return l