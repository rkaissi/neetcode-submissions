class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { ")":"(", "]":"[", "}":"{" }

        for c in s:
            if c not in hashmap:
                stack.append(c)
                continue
            
            if stack and stack[-1] == hashmap[c]:
                stack.pop()
            else:
                return False
        
        return not stack