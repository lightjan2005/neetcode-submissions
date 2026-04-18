class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numSet = set(nums)
        curMaxLength = 1
        
        for num in numSet:
            if num - 1 not in numSet:
                curLength = 1
                curNum = num
                while curNum + 1 in numSet:
                    curLength += 1
                    curNum += 1
                curMaxLength = max(curMaxLength, curLength)

        return curMaxLength