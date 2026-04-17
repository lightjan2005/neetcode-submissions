class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        sDict = collections.Counter(s)
        tDict = collections.Counter(t)

        # loop through s string and check both dictionaries 
        # if the char count is the same

        for c in s:
            if sDict[c] != tDict[c]: return False
        
        for c in t:
            if sDict[c] != tDict[c]: return False

        return True