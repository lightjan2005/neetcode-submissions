class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(start, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return
            
            for i in range(start, n+1):
                arr.append(i)
                dfs(i+1, arr)
                arr.pop()

        dfs(1,[])

        return res