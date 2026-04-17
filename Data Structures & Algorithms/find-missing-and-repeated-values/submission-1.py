class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        maxNum = n * n
        ans = [0 for i in range(2)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                else:
                    ans[0] = grid[i][j]
        
        for i in range(1, maxNum + 1):
            if i not in seen:
                ans[1] = i
        
        return ans
