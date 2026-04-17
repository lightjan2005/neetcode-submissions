class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        total = 0
        for operation in shift:
            direction = operation[0]
            amount = operation[1]
            if direction == 0:
                total -= amount
            else:
                total += amount

        dq = deque(s)
        dq.rotate(total)

        return s if total == 0 else ''.join(dq)