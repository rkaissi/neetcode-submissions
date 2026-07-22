class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freqMap = {}
        res = []

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        for n, c in freqMap.items():
            buckets[c].append(n)
        
        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                k -= 1

                if k <= 0:
                    return res
            

