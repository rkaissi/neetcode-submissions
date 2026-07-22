class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = []
        for n in nums:
            if n in numbers:
                return True
            numbers.append(n)
        return False
            