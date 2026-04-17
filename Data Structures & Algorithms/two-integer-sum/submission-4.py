class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numDict = {}
        ans = []

        for i,num in enumerate(nums):
            dif = target - num

            if dif in numDict:
                ans.append(numDict[dif])
                ans.append(i)
            else:
                numDict[num] = i

        return ans