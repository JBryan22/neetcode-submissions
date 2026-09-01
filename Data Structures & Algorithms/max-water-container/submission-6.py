class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            mostWater = max(mostWater, water)

            if heights[l] >= heights[r]:
                l += 1
            else:
                r -= 1
        return mostWater