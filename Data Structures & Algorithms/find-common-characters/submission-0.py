class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        numDict = Counter(words[0])

        for word in words:
            numDict &= Counter(word)

        return list(numDict.elements())