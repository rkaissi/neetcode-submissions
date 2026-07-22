class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            hashset[tuple(count)].append(s)
        return hashset.values()