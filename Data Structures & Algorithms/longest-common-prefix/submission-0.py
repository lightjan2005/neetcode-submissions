class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        for i in range(len(strs[0])):
            for string in strs:
                if i > len(string) - 1 or strs[0][i] != string[i]:
                    return res
            res += strs[0][i]

        return res