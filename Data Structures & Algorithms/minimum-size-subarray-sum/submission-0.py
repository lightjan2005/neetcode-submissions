class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        minLength = float("inf")
        l = 0
        curSum = 0
        
        for r in range(len(nums)):
            curSum += nums[r]
            if curSum >= target:
                while curSum >= target:
                    minLength = min(r-l+1, minLength)
                    curSum -= nums[l]
                    l += 1

        return 0  if minLength == float("inf") else minLength



        