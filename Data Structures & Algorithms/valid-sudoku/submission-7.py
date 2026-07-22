class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            rSet = set()
            for c in range(cols):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in rSet:
                    return False
                rSet.add(cell)
        
        for c in range(cols):
            cSet = set()
            for r in range(rows):
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in cSet:
                    return False
                cSet.add(cell)
        
        boxSets = [set() for i in range((rows // 3) * (cols // 3))]

        for r in range(rows):
            for c in range(cols):
                box = (r // 3) * 3 + (c // 3)
                cell = board[r][c]
                if cell == ".":
                    continue
                if cell in boxSets[box]:
                    return False
                boxSets[box].add(cell)
        
        return True