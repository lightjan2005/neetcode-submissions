class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = 0
        def dfs(i, curRes):
            nonlocal res
            if i == len(nums):
                res = res + curRes
                return

            dfs(i+1, curRes^nums[i])
            dfs(i+1, curRes)

        dfs(0,0)

        return res