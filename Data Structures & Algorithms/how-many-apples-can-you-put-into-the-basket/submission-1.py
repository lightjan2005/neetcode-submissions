class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        count = 0
        curSum = 0
        weight.sort()
        if weight[0] > 5000:
            return 0
        
        for w in weight:
            curSum += w
            count += 1
            if curSum > 5000:
                return count - 1

        return count