class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        res = []

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        buckets = [[] for _ in range(max(freqMap.values())+1)]

        for key, val in freqMap.items():
            buckets[val].append(key)
        print(buckets)
        
        for i in range(len(buckets)-1, -1, -1):
            for key in buckets[i]:
                if k <= 0:
                    break
                res.append(key)
                k -= 1
            
            if k <= 0:
                break
        
        return res