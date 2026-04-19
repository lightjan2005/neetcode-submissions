class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        res = ""
        l = 0
        needed = Counter(t)
        requiredKeys = len(needed)
        meetNeeded = 0
        curMaxLength = float("inf")
        sCount = {}

        for r,c in enumerate(s):
            if c in needed:
                sCount[c] = sCount.get(c,0) + 1
                if sCount[c] == needed[c]:
                    meetNeeded += 1
            
            while meetNeeded == requiredKeys:
                if (r-l+1) < curMaxLength:
                    curMaxLength = r-l+1
                    res = s[l:r+1]

                if s[l] in needed:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < needed[s[l]]:
                        meetNeeded -= 1
                l += 1

        return res