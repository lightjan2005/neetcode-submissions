class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        numDict = Counter(nums)
        
        i = 0
        for j in range(3):
            count = numDict[j]
            while count > 0:
                nums[i] = j
                i += 1
                count -= 1

