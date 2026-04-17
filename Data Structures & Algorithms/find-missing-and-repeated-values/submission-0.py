class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        n = len(grid)
        maxNum = n * n
        ans = [0 for i in range(2)]
        number = [i for i in range(1, maxNum + 1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                    number.remove(grid[i][j])
                else:
                    ans[0] = grid[i][j]
        ans[1] = number[0]
        
        return ans
