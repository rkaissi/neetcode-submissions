class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        
        combined = list(zip(position, speed))
        combined.sort(reverse=True, key=lambda e: e[0])

        for p, s in combined:
            timeToTarget = (target - p) / s
            res.append(timeToTarget)

        fleets = 1
        currentMaxTicks = res[0]
        for i in range(1, len(res)):
            if res[i] > currentMaxTicks:
                currentMaxTicks = res[i]
                fleets += 1

        return fleets