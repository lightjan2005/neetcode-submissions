class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1 for i in range(len(nums))]
        leftNums = [1 for j in range(len(nums))]
        rightNums = [1 for k in range(len(nums))]
        
        for a in range(1,len(nums)):
            leftNums[a] = leftNums[a-1] * nums[a-1]

        for b in range(len(nums)-2,-1,-1):
            rightNums[b] = rightNums[b+1] * nums[b+1]

        for c in range(len(nums)):
            output[c] = leftNums[c] * rightNums[c]

        return output