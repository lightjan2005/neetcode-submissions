class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        incoming = [0 for i in range(n+1)]
        outcoming = [0 for i in range(n+1)]

        for a,b in trust:
            outcoming[a] += 1
            incoming[b] += 1

        for i in range(1,n+1):
            if outcoming[i] == 0 and incoming[i] == n-1:
                return i

        return -1