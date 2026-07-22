class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = str(sorted(s))
            hashmap[key] = hashmap.get(key, []) + [s]
        return hashmap.values()