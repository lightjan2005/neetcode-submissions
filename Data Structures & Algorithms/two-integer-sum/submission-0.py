class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        ans = []
        for i, num in enumerate(nums):
            dif = target - num
            if dif in dic:
                ans = [dic[dif], i]
            else:
                dic[num] = i
        return ans