class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ROWS = len(picture)
        COLS = len(picture[0])
        countR = defaultdict(int) # {0: 1, 1: 1}
        countC = defaultdict(int) # {0: 1, 1: 1}
        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == 'B':
                    countR[r] += 1
                    countC[c] += 1

        for r in range(ROWS):
            for c in range(COLS):
                if picture[r][c] == 'B':
                    if countR[r] == 1 and countC[c] == 1:
                        ans += 1

        return ans
