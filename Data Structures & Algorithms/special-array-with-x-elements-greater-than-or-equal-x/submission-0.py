class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        maxNum = len(nums)
        r = 0
        for i in range(0, maxNum + 1):
            while r < len(nums) and nums[r] < i:
                r += 1
            if i == len(nums) - r:
                return i

        return -1