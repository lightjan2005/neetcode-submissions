class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] != 1:
                res = max(r-l, res)
                l = r + 1
        
        res = max(len(nums)-l, res)

        return res