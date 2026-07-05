class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curMax = -1
        count = 1
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                count += 1
            else:
                count = 1
            if count == 3:
                curMax = max(int(num[i]), curMax)


        return "" if curMax == -1 else 3 * str(curMax)
