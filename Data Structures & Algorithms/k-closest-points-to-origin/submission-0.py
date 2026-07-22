class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [(-self.distanceToOrigin(p), p) for p in points]
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        return [e[1] for e in maxHeap]

    def distanceToOrigin(self, point: List[int]):
        x, y = point
        return math.sqrt((x ** 2) + (y ** 2))