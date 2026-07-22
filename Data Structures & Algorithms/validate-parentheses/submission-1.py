class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in hashmap:
                if len(stack) == 0 or stack[-1] != hashmap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0