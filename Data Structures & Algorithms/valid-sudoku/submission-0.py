class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check row by row
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False

        # Check column by column
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    return False

        # Check sub-boxes
        seen = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in seen[(i//3),(j//3)]:
                    seen[(i//3),(j//3)].add(board[i][j])
                else:
                    return False

        return True