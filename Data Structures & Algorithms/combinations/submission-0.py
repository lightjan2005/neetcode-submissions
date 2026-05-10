class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        nums = [i for i in range(1,n+1)]

        def dfs(i, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            
            for idx in range(i, n):
                arr.append(nums[idx])
                dfs(idx+1, arr)
                arr.pop()

        dfs(0,[])

        return res