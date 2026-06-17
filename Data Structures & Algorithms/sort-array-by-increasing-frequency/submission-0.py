class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        countNums = Counter(nums)
        res = sorted(nums, key=lambda x: (countNums[x], -x))

        return res
