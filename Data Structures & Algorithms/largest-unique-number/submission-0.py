class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        numDict = Counter(nums)
        curMax = -1

        for i in range(len(nums)):
            if nums[i] > curMax and numDict[nums[i]] == 1:
                curMax = nums[i]


        return curMax