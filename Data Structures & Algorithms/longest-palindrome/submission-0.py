class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = Counter(s)
        res = 0
        seen = set()
        flag = 0
        for c in s:
            if c not in seen:
                seen.add(c)
                res += charCount[c] // 2
                if charCount[c] % 2 != 0:
                    flag = 1

        return res*2 + flag