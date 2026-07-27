class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxCount = 0
        for c in s:
            if c == '(':
                stack.append('(')

            elif c == ')':
                maxCount = max(maxCount, len(stack))
                stack.pop()

        return maxCount