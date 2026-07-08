class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter("".join(words))
        n = len(words)
        for char in counts:
            if counts[char] % n != 0:
                return False

        return True