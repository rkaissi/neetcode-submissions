class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            median = (l + r) // 2
            if target >= matrix[median][0] and target <= matrix[median][-1]:
                return self.binarySearch(matrix[median], target)
            elif target < matrix[median][0]:
                r = median - 1
            elif target > matrix[median][-1]:
                l = median + 1
        return False

    def binarySearch(self, arr, target):
        l, r = 0, len(arr) - 1
        
        while l <= r:
            median = (l + r) // 2
            if target == arr[median]:
                return True
            elif  target < arr[median]:
                r = median - 1
            elif target > arr[median]:
                l = median + 1
        return False