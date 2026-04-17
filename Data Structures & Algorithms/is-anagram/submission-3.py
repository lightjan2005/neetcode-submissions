class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sDict = {}
        tDict = {}

        for c in s:
            if c not in sDict:
                sDict[c] = 1
            else:
                sDict[c] += 1

        for c2 in t:
            if c2 not in tDict:
                tDict[c2] = 1
            else:
                tDict[c2] += 1

        return sDict == tDict