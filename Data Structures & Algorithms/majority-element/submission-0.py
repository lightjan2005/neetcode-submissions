class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        numDict = {}

        for num in nums:
            numDict[num] = numDict.get(num,0) + 1
            if numDict[num] > len(nums) // 2:
                return num

        return -1