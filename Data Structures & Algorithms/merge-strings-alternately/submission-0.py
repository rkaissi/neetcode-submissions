class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        minLen = min(len(word1), len(word2))
        for i in range(minLen):
            res.append(word1[i])
            res.append(word2[i])

        res.extend(word1[minLen:])
        res.extend(word2[minLen:])

        return "".join(res)