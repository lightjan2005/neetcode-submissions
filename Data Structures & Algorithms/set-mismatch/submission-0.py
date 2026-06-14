class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, 0

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                l = nums[i]
            elif nums[i] - 1 != nums[i-1]:
                r = nums[i-1] + 1
        
        if r == 0:
            if nums[0] != 1:
                r = 1
            else:
                r = n

        return [l,r]