class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        

        clean = s.rstrip()
        length = 0
        r = len(clean) - 1
        while r >= 0 and clean[r] != " ":
            length += 1
            r -= 1

        return length
