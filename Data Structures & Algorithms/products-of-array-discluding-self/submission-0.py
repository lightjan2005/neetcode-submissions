class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftArr = [1 for i in range(len(nums))]
        rightArr = [1 for i in range(len(nums))]
        ans = [1 for i in range(len(nums))]
        
        for i in range(1,len(nums)):
            leftArr[i] = leftArr[i-1] * nums[i-1]
        
        for j in range(len(nums)-2,-1,-1):
            rightArr[j] = rightArr[j+1] * nums[j+1]
        

        for k in range(len(nums)):
            ans[k] = leftArr[k] * rightArr[k]

        return ans