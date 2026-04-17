class Solution:
    def hammingWeight(self, n: int) -> int:
        
        newStr = bin(n)
        count = 0
        for c in newStr:
            if c == '1': 
                count += 1
        return count