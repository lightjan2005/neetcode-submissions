class Solution:
    def confusingNumber(self, n: int) -> bool:
        chars = list(str(n))
        invalid = ['2', '3', '4', '5', '7']
        charDict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}        
        newNum = []
        for c in chars:
            if c in invalid:
                return False
            else:
                newNum.append(charDict[c])

        return int("".join(newNum[::-1])) != n