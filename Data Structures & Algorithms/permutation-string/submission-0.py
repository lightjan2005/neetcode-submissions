class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        needed = [0] * 26
        currentWindow = [0] * 26
        for ch in s1:
            needed[ord(ch) - ord('a')] += 1
        for i in range(len(s1)):
            currentWindow[ord(s2[i]) - ord('a')] += 1        
        if needed == currentWindow: return True

        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            currentWindow[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            currentWindow[ord(s2[r]) - ord('a')] += 1
            if needed == currentWindow: return True 
        
        return False
                


        