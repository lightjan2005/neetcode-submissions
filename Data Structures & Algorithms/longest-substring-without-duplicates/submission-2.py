class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        maxLength = 0
        for i in range(len(s) - 1):
            strSet = set()
            j = i + 1
            if s[i] == s[j]:
                maxLength = max(maxLength,1)
                continue
            strSet.add(s[i])
            while j < len(s) and s[j] not in strSet:
                strSet.add(s[j])
                j += 1
            maxLength = max(maxLength, j-i)
            strSet.clear()
        return maxLength
            
