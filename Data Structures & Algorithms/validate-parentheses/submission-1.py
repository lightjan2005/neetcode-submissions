class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mappings = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in mappings.values():
                stack.append(c)
            elif c in mappings:
                if not stack or stack[-1] != mappings[c]:
                    return False
                stack.pop()

        return len(stack) == 0