class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height) - 1
        preArr = [0] * len(height)
        sufArr = [0] * len(height)
        totalArea = 0

        # Get the max for pre-index
        for i in range(1,len(height)):
            preArr[i] = max(preArr[i-1], height[i-1])
        # Get the max for suf-index
        for j in range(len(height)-2, -1, -1):
            sufArr[j] = max(sufArr[j+1], height[j+1])
        
        # Calculate the trapped water 
        for i in range(len(height)):
            totalArea += max(0,min(preArr[i], sufArr[i]) - height[i])

        return totalArea
