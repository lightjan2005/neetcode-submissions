class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r = 0, 0

        while r < len(abbr):
            if abbr[r].isalpha():
                if l >= len(word) or abbr[r] != word[l]:
                    return False
                r += 1
                l += 1
            else:
                # get the num in the abbreaviation string
                if abbr[r] == '0':
                    return False
                numStr = ""
                while r < len(abbr) and abbr[r].isdigit():
                    numStr += abbr[r]
                    r += 1
                num = int(numStr)
                l += num

        return l == len(word)