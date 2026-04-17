class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxLength = 0
        numSet = set(nums)

        for num in nums:
            if num - 1 not in numSet:
                curLength = 1
                while num+curLength in numSet:
                    curLength += 1 

                maxLength = max(curLength, maxLength)

        return maxLength