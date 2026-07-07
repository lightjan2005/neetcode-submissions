class Solution:
    def maxScore(self, s: str) -> int:
        count = Counter(s)
        rightScore = count['1']
        leftScore = 0
        res = 0
        
        for i in range(len(s) - 1):
            c = s[i]
            if c == '0':
                leftScore += 1
            else:
                rightScore -= 1
            res = max(res, leftScore + rightScore)

        return res