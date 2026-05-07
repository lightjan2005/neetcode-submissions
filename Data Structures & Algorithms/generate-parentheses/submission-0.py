class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, o, c):
            if c > o or o > n:
                return
            if len(s) == 2 * n:
                res.append("".join(s.copy()))
                return
            
            s.append('(')
            dfs(s, o + 1, c)
            s.pop()

            s.append(')')
            dfs(s, o, c + 1)
            s.pop()
        
        dfs([], 0, 0)

        return res