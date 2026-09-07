class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        res = 0

        def bfs(beginR, beginC):
            q = deque([(beginR, beginC)])
            visited.add((beginR, beginC))
            area = 1

            while q:
                (r, c) = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r+dr, c+dc

                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and (nr, nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, bfs(r, c))
        
        return res