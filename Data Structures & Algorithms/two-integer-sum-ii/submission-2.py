class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = []

        for i, n in enumerate(numbers):
            if len(idx) > 0 and target - n == numbers[idx[0]-1]:
                idx.append(i + 1)
                return idx
            if ((target - n) in numbers[i:]) and len(idx) == 0:
                idx.append(i + 1)
        return idx