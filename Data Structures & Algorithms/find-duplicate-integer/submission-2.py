class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            val = abs(num)
            index = val - 1
            if nums[index] < 0:
                return val
            nums[index] = -nums[index]

        return 0