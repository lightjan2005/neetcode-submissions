class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordArr = s.split(' ')
        wordDict = {}
        seen = set()
        if len(pattern) != len(wordArr):
            return False

        for i, c in enumerate(pattern):
            if c not in wordDict:
                if wordArr[i] in seen:
                    return False
                seen.add(wordArr[i])
                wordDict[c] = wordArr[i]
            else:
                if wordDict[c] != wordArr[i]:
                    return False
                

        return True