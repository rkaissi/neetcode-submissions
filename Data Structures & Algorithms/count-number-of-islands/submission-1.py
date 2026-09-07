from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited = {}
        res = 0

        def bfs(beginR, beginC):
            q = deque([(beginR, beginC)])
            self.visited[(beginR, beginC)] = True

            while q:
                (r, c) = q.popleft()
                
                for dr, dc in DIRS:
                    nr, nc = r+dr, c+dc

                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and (nr, nc) not in self.visited and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        self.visited[(nr, nc)] = True

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in self.visited:
                    bfs(r, c)
                    res += 1
        
        return res