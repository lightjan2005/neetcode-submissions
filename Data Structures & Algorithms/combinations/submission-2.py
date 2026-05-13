class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def dfs(num, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            for j in range(num, n+1):
                arr.append(j)
                dfs(j+1, arr)
                arr.pop()

        dfs(1,[])
        return res