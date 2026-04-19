class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,0
        seen = set()
        maxLength = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            maxLength = max(maxLength, r-l)

        return maxLength
