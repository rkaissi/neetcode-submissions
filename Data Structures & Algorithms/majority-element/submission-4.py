class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0

        for n in nums:
            if element is None:
                element = n
            if element == n:
                count += 1
            else:
                count -= 1
            
            if count <= 0:
                element = n
                count = 1
        
        return element
