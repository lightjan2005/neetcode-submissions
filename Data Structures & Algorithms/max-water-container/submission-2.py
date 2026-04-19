class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxAmount = 0

        l, r = 0, len(heights) - 1

        while l < r:
            curArea = 0
            if heights[l] < heights[r]:
                curArea = heights[l] * (r-l)
                l += 1
            else:
                curArea = heights[r] * (r-l)
                r -= 1
            maxAmount = max(curArea,maxAmount)


        return maxAmount