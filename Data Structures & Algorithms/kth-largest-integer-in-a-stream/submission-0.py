class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.minHeap = []

        for n in nums:
            if len(self.minHeap) < self.k:
                heapq.heappush(self.minHeap, n)
            else:
                heapq.heappushpop(self.minHeap, n)


    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            heapq.heappushpop(self.minHeap, val)

        return self.minHeap[0]