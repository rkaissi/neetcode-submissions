import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hs = set()
            for elem in row:
                if elem in hs:
                    return False
                if elem != ".":
                    hs.add(elem)
        
        rows = len(board)
        cols = len(board[0])
        for c in range(cols):
            hs = set()
            for r in range(rows):
                elem = board[r][c]
                if elem in hs:
                    return False
                if elem != ".":
                    hs.add(elem)
        
        sSets = [set() for i in range(math.ceil(r/3)*math.ceil(c/3))]
        for r in range(rows):
            for c in range(cols):
                square = (r // 3) * 3 + (c // 3)
                elem = board[r][c]
                if elem in sSets[square]:
                    return False
                if elem != ".":
                    sSets[square].add(elem)
        return True