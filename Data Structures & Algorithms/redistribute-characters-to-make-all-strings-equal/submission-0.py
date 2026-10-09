class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        charFreq = {}
        n = len(words)

        for word in words:
            for c in word:
                charFreq[c] = 1 + charFreq.get(c, 0)

        for freq in charFreq.values():
            if freq % n != 0:
                return False
        
        return True