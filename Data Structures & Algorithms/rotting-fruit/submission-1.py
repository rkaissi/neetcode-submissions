from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            rotted = False
            for _ in range(len(q)):
                (r, c) = q.popleft()
                print((r, c))
                
                for dr, dc in DIRS:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        rotted = True
            res += 1 if rotted else False
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return res


    [[2,1,1],
     [2,1,0],
     [0,1,1]]