class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i,curSum, arr):
            if curSum == target:
                res.append(arr.copy())
                return
            if curSum > target or i == len(candidates):
                return

            arr.append(candidates[i])
            dfs(i+1, curSum + candidates[i], arr)
            arr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curSum, arr)


        dfs(0,0,[])

        return res