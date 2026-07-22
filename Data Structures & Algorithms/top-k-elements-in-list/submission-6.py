class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, value in count.items():
            freq[value].append(key)
        
        output = []
        index = len(freq) - 1

        while k > 0 and index > 0:
            for n in freq[index]:
                if k > 0:
                    output.append(n)
                    k -= 1
            index -= 1
        
        return output