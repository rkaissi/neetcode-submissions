import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # t = (target - position) / speed
        time = []
        res = 1

        for p, s in sorted(zip(position, speed), key=lambda e: e[0], reverse=True):
            t = (target - p) / s
            time.append(t)
        
        print(time)
        maxFleet = time[0]
        for i in range(1, len(time)):
            if time[i] > maxFleet:
                maxFleet = time[i]
                res += 1

        return res