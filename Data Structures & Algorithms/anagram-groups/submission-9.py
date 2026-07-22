from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[self.getAscii(c)] += 1
            
            hashmap[tuple(key)].append(s)
        
        return list(hashmap.values())
        
    def getAscii(self, char):
        return ord(char) - ord("a")
