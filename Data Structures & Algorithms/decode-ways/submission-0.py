from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            if i == len(s) - 1 or int(s[i:i+2]) > 26:
                # have to take 1
                return dfs(i+1)
            elif s[i+1] == '0':
                #have to take 2
                return dfs(i+2)
            
            return dfs(i+1) + dfs(i+2)
        
        return dfs(0)