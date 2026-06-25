class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charDict = Counter(magazine)
        ransomDict = Counter(ransomNote)
        for c in ransomNote:
            if ransomDict[c] > charDict[c]:
                return False

        return True