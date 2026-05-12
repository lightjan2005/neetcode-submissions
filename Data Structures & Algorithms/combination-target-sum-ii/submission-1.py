class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curSum, arr):
            if curSum == target:
                res.append(arr.copy())
                return
            if curSum > target:
                return

            # [1,2,2,4,5,6,9]
            for j in range(i, len(candidates)):
                if j > i and candidates[j] ==  candidates[j-1]:
                    continue
                arr.append(candidates[j])
                dfs(j+1, curSum + candidates[j], arr)
                arr.pop()

        dfs(0,0,[])

        return res