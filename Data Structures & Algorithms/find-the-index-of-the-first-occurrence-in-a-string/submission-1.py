class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        l,r = 0,0
        count = 0
        while l < len(haystack):
            i = l
            r = 0
            count = 0
            while i < len(haystack) and r < len(needle) and haystack[i] == needle[r]:
                i += 1
                r += 1
                count += 1
                if count == len(needle):
                    return l
            l += 1

        return -1