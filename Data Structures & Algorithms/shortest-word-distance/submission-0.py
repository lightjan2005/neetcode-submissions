class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        curMin = float("inf")
        x,y = -1,-1

        for i,word in enumerate(wordsDict):
            if word == word1:
                x = i
            elif word == word2:
                y = i
            if x != -1 and y!= -1:
                curMin = min(curMin, abs(x-y))

        return curMin