class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        res = ""
        needed = {}
        l = 0
        
        # get needed 
        for ch in t:
            needed[ch] = needed.get(ch,0) + 1

        requiredKeys = len(needed)
        meetNeeded = 0
        curMaxLength = float("inf")

        sCount = {}
        for r,c in enumerate(s):
            # if meets window we need to add to the dictionary and update
            # meet needed
            if c in needed:
                sCount[c] = sCount.get(c,0) + 1
                if sCount[c] == needed[c]:
                    meetNeeded += 1

            # shrink window
            while meetNeeded == requiredKeys:
                # update the currentMaxLength and string
                if (r-l+1) < curMaxLength:
                    curMaxLength = (r-l+1)
                    res = s[l:r+1]

                if s[l] in needed:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < needed[s[l]]:
                        meetNeeded -= 1
                l+= 1
        return res