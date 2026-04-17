class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        total = 0
        newStr = ""
        for operation in shift:
            direction = operation[0]
            amount = operation[1]
            if direction == 0:
                total -= amount
            else:
                total += amount

        if total == 0:
            return s
        else:
            dq = deque(s)
            dq.rotate(total)
            newStr = ''.join(dq)

        return newStr