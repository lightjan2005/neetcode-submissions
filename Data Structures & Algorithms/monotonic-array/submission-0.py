class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:        
        
        isIncreasing = True
        isDecreasing = True
        allSame = True
        # increasing
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                isIncreasing = False
            if nums[i] > nums[i-1]:
                isDecreasing = False
            if nums[i] != nums[i-1]:
                allSame = False

        return isIncreasing or isDecreasing or allSame