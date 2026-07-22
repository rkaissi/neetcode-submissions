class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c in hashmap:
                if len(stack) == 0 or stack.pop() != hashmap[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0