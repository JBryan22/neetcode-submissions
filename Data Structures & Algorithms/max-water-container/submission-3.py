class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            mostWater = max(mostWater, water)

            if abs(heights[l + 1] - heights[l]) < abs(heights[r - 1] - heights[r]):
                l += 1
            else:
                r -= 1
        return mostWater