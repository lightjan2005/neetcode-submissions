class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        l = 0
        if len(s) == 0: return True

        for i in range(len(t)):
            if s[l] == t[i]:
                l += 1
            if l == len(s):
                return True
            
        return l == len(s)