class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # minimize the max value on the path
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        minHeap = [(grid[0][0], (0, 0))]
        visited = set()

        while minHeap:
            elev, (r, c) = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (ROWS-1, COLS-1):
                return elev
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and (nr, nc) not in visited:
                    newMax = max(elev, grid[nr][nc])
                    heapq.heappush(minHeap, (newMax, (nr, nc)))
        