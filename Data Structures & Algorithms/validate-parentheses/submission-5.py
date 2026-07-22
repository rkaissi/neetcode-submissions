class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in hashmap:
                stack.append(c)
                continue
            if not stack or stack.pop() != hashmap[c]:
                return False
        return len(stack) == 0