class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            li = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                li[index] += 1
            hm[tuple(li)] = hm.get(tuple(li), []) + [s]
        
        return hm.values()


