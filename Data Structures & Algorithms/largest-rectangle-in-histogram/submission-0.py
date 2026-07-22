class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            currIdx = i
            while stack and h < stack[-1][1]:
                stackI, stackH = stack.pop()
                w = i - stackI
                area = w * stackH
                maxArea = max(maxArea, area)
                currIdx = stackI
            
            stack.append((currIdx, h))
        
        for i, h in stack:
            w = len(heights) - i
            area = w * h
            maxArea = max(maxArea, area)
        
        return maxArea
