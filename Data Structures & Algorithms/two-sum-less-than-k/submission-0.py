class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1

        nums.sort()
        l, r = 0, len(nums) - 1

        maxSum = -1

        while l < r:
            curSum = nums[l] + nums[r]
            if curSum < k:
                l += 1
                maxSum = max(maxSum, curSum)
            else:
                r -= 1

        return maxSum