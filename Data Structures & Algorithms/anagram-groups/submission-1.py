class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            hashmap[key].append(s)
        return hashmap.values()