class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2Set = set(arr2)
        arr1Map = {}
        end = []

        for elem in arr1:
            if elem not in arr2Set:
                end.append(elem)
            arr1Map[elem] = 1 + arr1Map.get(elem, 0)
        end.sort()
        
        res = []
        for elem in arr2:
            for i in range(arr1Map[elem]):
                res.append(elem)

        return res + end