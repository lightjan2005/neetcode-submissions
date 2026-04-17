class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            row = []
            if i == 0:
                row = [1]
            elif i == 1:
                row = [1,1]
            else:
                for j in range(i + 1):
                    if j == 0 or j == i:
                        row.append(1)
                    else:
                        row.append(res[i-1][j-1] + res[i-1][j])
            res.append(row)
                        
        return res