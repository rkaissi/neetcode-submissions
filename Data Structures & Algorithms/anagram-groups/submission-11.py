from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)

        for s in strs:
            freqList = [0] * 26
            for c in s:
                freqList[ord(c) - ord("a")] += 1
            
            freqMap[tuple(freqList)].append(s)
        
        return list(freqMap.values())