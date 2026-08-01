class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            remain = columnNumber % 26
            c = columnNumber // 26
            res = (chr(remain+65)) + res

            columnNumber = c

        return res