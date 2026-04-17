class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        count = Counter(s)
        countOdd = 0

        for v in count.values():
            if v % 2 == 1:
                countOdd += 1
            if countOdd > 1:
                return False
            

        return True