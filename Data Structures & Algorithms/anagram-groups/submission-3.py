from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        # O(m*n*26) = O(m*n) where n is the length of the strs array
        for string in strs:
            # O(m * 26) = O(m) where m is the length of the string
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            hashmap[tuple(count)].append(string)
        return hashmap.values()

# lists in python can't be dict keys, so use a tuple instead: tuple([])
# use ord to get ascii position of char e.g. ord("a")
# do ord(char) - ord("a") to get relative poisiton in alphabet from 0