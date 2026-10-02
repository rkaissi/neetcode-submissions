from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, tgt, time in times:
            adj[src].append((tgt, time))
        
        visited = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)

            res = max(res, t1)
            for n2, t2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (t1+t2, n2))
        
        for i in range(1, n+1):
            if i not in visited:
                return -1
        
        return res