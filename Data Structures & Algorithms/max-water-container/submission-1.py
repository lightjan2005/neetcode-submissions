class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxAmount = 0

        l,r = 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                curAmount = heights[l] * (r-l)
                maxAmount = max(curAmount, maxAmount)
                l += 1
            else:
                curAmount = heights[r] * (r-l)
                maxAmount = max(curAmount, maxAmount)
                r -= 1
        
        return maxAmount