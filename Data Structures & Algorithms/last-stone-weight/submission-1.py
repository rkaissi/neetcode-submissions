class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)

            diff = first - second
            if diff > 0:
                heapq.heappush(maxHeap, -diff)
            
        return -maxHeap[0] if maxHeap else 0


        # 2 3 6 2 4
        # 6 4 3 2 2
        # Stones: 6 4 -- Array: 3 2 2
        # Get 2 -- Array: 3 2 2 2
        # 3 2
        # 1
        # 2 2 1
        # 2 2
        # 1