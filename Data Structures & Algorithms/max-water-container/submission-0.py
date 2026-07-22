class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            area = w * h
            maxA = max(maxA, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxA