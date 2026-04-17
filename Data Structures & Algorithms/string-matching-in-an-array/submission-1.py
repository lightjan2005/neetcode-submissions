class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for word in words:
            for word2 in words:
                if word != word2 and word in word2 and word not in res:
                    res.append(word)
            
        return res