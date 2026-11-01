class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqMap = {}
        res = []
        n = len(nums)

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        for num, freq in freqMap.items():
            if freq > math.floor(n/3):
                res.append(num)
        
        return res