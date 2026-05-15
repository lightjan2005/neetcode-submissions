class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        sToT = {}
        tToS = {}
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            
            if charS in sToT and sToT[charS] != charT:
                return False
            if charT in tToS and tToS[charT] != charS:
                return False
                
            sToT[charS] = charT
            tToS[charT] = charS

        return True