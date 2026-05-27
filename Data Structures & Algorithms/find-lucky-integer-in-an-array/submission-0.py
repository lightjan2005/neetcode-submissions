class Solution:
    def findLucky(self, arr: List[int]) -> int:
        countNums = Counter(arr)
        curMax = -1
        for num in arr:
            if num == countNums[num]:
                curMax = max(curMax, num)


        return curMax