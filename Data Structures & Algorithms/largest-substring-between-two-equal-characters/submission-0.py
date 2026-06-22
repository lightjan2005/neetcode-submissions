class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        sDict = {}
        maxLength = -1
        for i,c in enumerate(s):
            if c not in sDict:
                sDict[c] = i
            else:
                maxLength = max(maxLength, i - sDict[c]-1)

        
        return maxLength