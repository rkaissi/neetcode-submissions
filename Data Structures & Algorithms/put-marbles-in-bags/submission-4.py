class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # [[5][7,9,5]]
        # [[5, 7][9,5]]
        # [[5, 7, 9][5]]
        # boundaries always included in the score

        # need k-1 pair sums

        # k-1 elems in min/maxheap
        if k == 1:
            return 0

        minHeap = []
        maxHeap = []
        n = len(weights)
        for i in range(n-1):
            pair = weights[i] + weights[i+1]
            if len(minHeap) < k-1:
                heapq.heappush(minHeap, pair)
            elif pair > minHeap[0]:
                heapq.heappushpop(minHeap, pair)
            
            if len(maxHeap) < k-1:
                heapq.heappush(maxHeap, -pair)
            elif -pair > maxHeap[0]:
                heapq.heappushpop(maxHeap, -pair)
        
        minWeight = -sum(maxHeap)
        maxWeight = sum(minHeap)

        return maxWeight - minWeight