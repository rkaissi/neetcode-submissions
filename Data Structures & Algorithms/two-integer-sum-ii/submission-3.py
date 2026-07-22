class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1

        # idx = []

        # for i, n in enumerate(numbers):
        #     if len(idx) > 0 and target - n == numbers[idx[0]-1]:
        #         idx.append(i + 1)
        #         return idx
        #     if ((target - n) in numbers[i:]) and len(idx) == 0:
        #         idx.append(i + 1)
        # return idx