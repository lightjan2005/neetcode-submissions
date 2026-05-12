class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(i, curSum, arr):
            if curSum == target:
                res.append(arr.copy())
                return
            if curSum > target:
                return
            
            for j in range(i, len(nums)):
                arr.append(nums[j])
                dfs(j, curSum + nums[j], arr)
                arr.pop()

        dfs(0,0,[])
        return res