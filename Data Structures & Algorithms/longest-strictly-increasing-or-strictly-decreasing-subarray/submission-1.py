class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        curMaxLength1 = 1
        curLength = 1
        # find the longest increasing
        for i in range(1,len(nums)):
            if nums[i - 1] > nums[i]:
                curLength += 1
            else:
                curLength = 1
            curMaxLength1 = max(curMaxLength1, curLength)
        print(curMaxLength1)


        # find the longest decreasing
        curMaxLength2 = 1
        curLength = 1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                curLength += 1
            else:
                curLength = 1
            curMaxLength2 = max(curMaxLength2, curLength)

        return max(curMaxLength1,curMaxLength2)