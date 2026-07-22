class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = [0, 0]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        count = [item[0] for item in sorted(count.items(), key=lambda item: item[1])]

        return count[-k:]