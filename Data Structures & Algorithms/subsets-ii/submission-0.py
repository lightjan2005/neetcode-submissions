class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, arr):
            if i == len(nums):
                res.append(arr.copy())
                return
            
            # Decision to include nums[i]
            arr.append(nums[i])
            dfs(i+1, arr)
            arr.pop()

            # Decision NOT to include nums[i] and all its duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i+1, arr)
        
        dfs(0,[])

        return res