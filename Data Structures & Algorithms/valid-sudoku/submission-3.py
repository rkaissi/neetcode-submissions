class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for elem in row:
                if elem == ".":
                    continue
                if elem in rowSet:
                    return False
                rowSet.add(elem)
        
        column = 0

        while column < len(board[0]):
            columnSet = set()
            for row in range(len(board)):
                elem = board[row][column]
                if elem == ".":
                    continue
                if elem in columnSet:
                    return False
                columnSet.add(elem)
            column += 1
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                subSet = set()
                for i in range(3):  # iterate over the 3 rows in each subgrid
                    for j in range(3):  # iterate over the 3 columns in each subgrid
                        elem = board[box_row + i][box_col + j]
                        if elem == ".":
                            continue
                        if elem in subSet:
                            return False
                        subSet.add(elem)
        
        return True