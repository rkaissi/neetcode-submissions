class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # maxHeap
        self.rightHeap = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)

        if len(self.leftHeap) > 0 and len(self.rightHeap) > 0 and -self.leftHeap[0] > self.rightHeap[0]:
            val = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, val)

        while len(self.leftHeap) - len(self.rightHeap) >= 2:
            val = -heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, val)
        
        while len(self.rightHeap) - len(self.leftHeap) >= 2:
            val = -heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, val)

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0]) / 2
        else:
            return -self.leftHeap[0] if len(self.leftHeap) > len(self.rightHeap) else self.rightHeap[0]
