class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, val in count.items():
            freq[val].append(n)
        
        res = []
        for i in range(len(nums), -1, -1):
            for n in freq[i]:
                if k <= 0:
                    return res
                res.append(n)
                k -= 1
        
        return res
