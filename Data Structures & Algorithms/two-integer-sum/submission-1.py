class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        ans = []

        for i,num in enumerate(nums):
            ansNum = target - nums[i]
            if ansNum in dic:
                ans = [dic[ansNum], i]
            else:
                dic[num] = i

        return ans