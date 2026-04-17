class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        sDict = Counter(s)
        tDict = Counter(t)

        return sDict == tDict