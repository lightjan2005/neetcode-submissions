class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = []
        for s in strs:
            num = len(s)
            newStr.append(str(num))
            newStr.append('#')
            newStr.append(s)
        return "".join(newStr)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        num = ""
        while i < len(s):

            if s[i] == '#':
                ans.append(s[i+1:i+1+int(num)])
                i += int(num) + 1
                num = ""
            elif s[i].isdigit():
                num += s[i]
                i += 1
        return ans
