class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        l = 0 
        count = 0
        for r in range(len(s)):
            if l == len(t):
                break
            if s[r] == t[l]:
                count += 1
                l += 1

        return len(t) - l