class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def calDays(capacity):
            curLoad = 0
            daysUsed = 1
            for weight in weights:
                if curLoad + weight > capacity:
                    daysUsed += 1
                    curLoad = 0
                curLoad += weight
            return daysUsed <= days

        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l+r)//2
            if calDays(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l

            