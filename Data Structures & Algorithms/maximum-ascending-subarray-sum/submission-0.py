class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float("-inf")

        for i,num in enumerate(nums):
            if i == 0:
                curSum += num
            else:
                if num > nums[i-1]:
                    curSum += num
                else:
                    curSum = num
            maxSum = max(maxSum, curSum)

        return maxSum
