class Solution:
    def isPalindrome(self, s: str) -> bool:

        formattedString = ""
        
        for c in s:
            if c.isalnum():
                formattedString += c

        l = 0
        r = len(formattedString) - 1

        while l <= r:
            if formattedString[l].lower() != formattedString[r].lower():
                return False
            l += 1
            r -= 1

        return True