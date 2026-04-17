class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        ans = []

        numDict = {'1': '1', '6': '9', '8':'8', '9':'6', '0': '0'}
        for i in range(len(num)):
            if num[i] not in numDict:
                return False
            ans.append(numDict[num[i]])

        newString = "".join(ans)
        return num == newString[::-1]