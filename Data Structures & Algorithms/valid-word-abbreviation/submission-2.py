class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(abbr):
            c = abbr[i]
            if c == "0":
                return False
            elif ord("1") <= ord(c) <= ord("9"):
                num = ""
                while i < len(abbr) and ord("0") <= ord(abbr[i]) <= ord("9"):
                    num += abbr[i]
                    i += 1
            
                j += int(num)
                if j > len(word):
                    return False
            else:
                if j >= len(word) or c != word[j]:
                    return False
                i += 1
                j += 1
        
        return j == len(word)

