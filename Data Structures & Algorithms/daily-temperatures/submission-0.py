class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack or t <= stack[-1][1]:
                stack.append((i, t))
                continue

            while stack and t > stack[-1][1]:
                idx, elem = stack.pop()
                output[idx] = i - idx
            stack.append((i, t))
            
        return output