class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countChars = Counter(chars)
        wordDict = []
        res = 0
        for word in words:
            wordDict = Counter(word)
            is_good = True
            for c in wordDict:
                if wordDict[c] > countChars[c]:
                    is_good = False
                    break
            if is_good:
                res += len(word)

        return res