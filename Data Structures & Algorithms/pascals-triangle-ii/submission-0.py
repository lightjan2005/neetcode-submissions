class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]

        dp = [[1],[1,1]]

        for i in range(2, rowIndex + 1):
            arr = [1 for i in range(i+1)]
            for j in range(i + 1):
                if j != 0 and j != i:
                    arr[j] = dp[i-1][j-1] + dp[i-1][j]
            dp.append(arr)

        return dp[rowIndex]
