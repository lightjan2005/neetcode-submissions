class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        initial = image[sr][sc]
        if initial == color:
            return image
        def dfs(r,c):
            if r > m - 1 or r < 0 or c > n - 1 or c < 0:
                return

            if image[r][c] == initial:
                image[r][c] = color
            else:
                return
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image