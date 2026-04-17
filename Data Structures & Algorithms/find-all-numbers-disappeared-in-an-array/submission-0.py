class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        arr = list(range(1, n + 1))
        for i in range(len(nums)):
            if nums[i] in arr:
                arr.remove(nums[i])
        
        return arr

        
