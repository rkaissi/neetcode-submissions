class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queryN = len(queries)
        res = [0] * queryN
        intervals.sort(key=lambda i: i[0])
        queriesTagged = list(zip(queries, list(range(queryN))))
        queriesTagged.sort(key=lambda i: i[0])
        minHeap = []
        i = 0

        for query, idx in queriesTagged:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i][0], intervals[i][1]
                size = end - start + 1
                heapq.heappush(minHeap, (size, end))
                i += 1
            
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)
            res[idx] = minHeap[0][0] if minHeap else -1
        
        return res