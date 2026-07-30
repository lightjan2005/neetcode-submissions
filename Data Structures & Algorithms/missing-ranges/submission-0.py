class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        nums = [lower - 1] + nums + [upper + 1]

        for i in range(len(nums)-1):
            arr = []
            if nums[i]+1 != nums[i+1]:
                arr.append(nums[i]+1)
                arr.append(nums[i+1]-1)
                res.append(arr)
        return res