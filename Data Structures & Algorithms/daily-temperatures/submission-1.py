class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                idx, elem = stack.pop()
                output[idx] = i - idx
            stack.append((i, t))
            
        return output