from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # bfs from atlantic cells and bfs from pacific cells and see overlap
        atlantic = set()
        pacific = set()

        atlanticQ = deque()
        pacificQ = deque()

        for c in range(COLS):
            pacificQ.append((0, c))
            pacific.add((0, c))
        
        for r in range(1, ROWS):
            pacificQ.append((r, 0))
            pacific.add((r, 0))
        
        for c in range(COLS):
            atlanticQ.append((ROWS-1, c))
            atlantic.add((ROWS-1, c))
        
        for r in range(ROWS-1):
            atlanticQ.append((r, COLS-1))
            atlantic.add((r, COLS-1))
        
        while atlanticQ:
            (r, c) = atlanticQ.popleft()
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in atlantic:
                    atlanticQ.append((nr, nc))
                    atlantic.add((nr, nc))
        
        while pacificQ:
            (r, c) = pacificQ.popleft()
            for dr, dc in DIRS:
                nr, nc = r+dr, c+dc
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in pacific:
                    pacificQ.append((nr, nc))
                    pacific.add((nr, nc))
        
        return [list(elem) for elem in list(atlantic & pacific)]