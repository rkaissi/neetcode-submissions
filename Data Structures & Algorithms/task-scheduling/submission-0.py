class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = Counter(tasks)
        maxHeap = [-count for count in hashmap.values()]
        heapq.heapify(maxHeap)
        time = 0
        
        queue = deque()
        while maxHeap or queue:
            time += 1
            
            if not maxHeap: # optional to skip idle times
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time