class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        self.perimeter = 0
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                self.perimeter += 1
                return
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1,c)
            dfs(r-1,c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return self.perimeter

        return self.perimeter