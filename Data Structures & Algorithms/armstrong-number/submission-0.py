class Solution:
    def isArmstrong(self, n: int) -> bool:
        num = str(n)
        digits = len(num)
        res = 0
        for c in num:
            res += math.pow(int(c),digits)

        return res == n