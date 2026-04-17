class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        def calCoins(num: int) -> int:
            return (1 + num)* num / 2

        l, r = 1, n

        while l <= r:
            mid = (l+r)//2
            if calCoins(mid) == n:
                return mid
            elif calCoins(mid) < n:
                l = mid + 1
            else:
                r = mid - 1

        return r
