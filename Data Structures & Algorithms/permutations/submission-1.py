class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i, arr):
            if i == len(nums):
                res.append(arr.copy())
                return

            for j in range(len(nums)):
                if nums[j] in arr:
                    continue
                arr.append(nums[j])
                dfs(i+1,arr)
                arr.pop()

        dfs(0,[])
        return res