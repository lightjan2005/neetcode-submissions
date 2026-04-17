class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        keyboardDict = {}
        for i,c in enumerate(keyboard):
            keyboardDict[c] = i

        moves = keyboardDict[word[0]]
        if len(word) == 1:
            return moves
        for i in range(1,len(word)):
            moves += abs(keyboardDict[word[i]] - keyboardDict[word[i-1]])

        return moves