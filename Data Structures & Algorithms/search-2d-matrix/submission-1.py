class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                row = matrix[m]
                l2, r2 = 0, len(row) - 1

                while l2 <= r2:
                    m2 = (l2 + r2) // 2

                    if row[m2] > target:
                        r2 = m2 - 1
                    elif row[m2] < target:
                        l2 = m2 + 1
                    else:
                        return True
                break
        
        return False
