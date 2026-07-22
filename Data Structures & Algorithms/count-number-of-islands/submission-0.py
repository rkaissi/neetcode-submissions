class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(x, y):
            q = deque([(x, y)])
            visited.add((x, y))
            while q:
                x, y = q.popleft()
                for (dx, dy) in dirs:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or ny < 0 or nx >= cols or ny >= rows or grid[ny][nx] == "0" or (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    q.append((nx, ny))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (c, r) not in visited:
                    bfs(c, r)
                    res += 1
        
        return res