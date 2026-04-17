class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count += 1

        ans = count
        r = k
        l = 0
        while r < len(blocks):
            if blocks[l] == 'W':
                count -= 1
            if blocks[r] == 'W':
                count += 1
            ans = min(ans, count)
            r += 1
            l += 1

        return ans