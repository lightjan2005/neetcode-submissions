class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) %2 != 0:
            return False
        pairs = len(nums)//2
        nums.sort()

        i = 0
        while i < len(nums):
            num1 = nums[i]
            num2 = nums[i+1]
            if num1 != num2:
                return False
            i += 2

        return True