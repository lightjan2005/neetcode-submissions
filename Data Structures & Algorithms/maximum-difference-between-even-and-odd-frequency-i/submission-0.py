class Solution:
    def maxDifference(self, s: str) -> int:
        
        count = Counter(s)
        ans = float("-inf")
        
        for odd in count.values():
            if odd % 2 == 0: continue
            for even in count.values():
                if even % 2 == 1: continue
                ans = max(ans, odd - even)

        return ans