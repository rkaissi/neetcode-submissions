class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        subsets = [set() for _ in range(rows * cols)]

        for r in range(rows):
            rowset = set()
            for c in range(cols):
                digit = board[r][c]
                if digit in rowset:
                    return False
                if digit != ".":
                    rowset.add(digit)
                
                subsetIdx = ((r // 3) * (cols // 3)) + (c // 3)
                subset = subsets[subsetIdx]
                if digit in subset:
                    return False
                if digit != ".":
                    subset.add(digit)
        
        for c in range(cols):
            colset = set()
            for r in range(rows):
                digit = board[r][c]
                if digit in colset:
                    return False
                if digit != ".":
                    colset.add(digit)
        
        return True