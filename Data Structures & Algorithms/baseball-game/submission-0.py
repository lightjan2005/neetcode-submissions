class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == '+':
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1+num2)
            elif operation == 'C':
                stack.pop()
            elif operation == 'D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(operation))
        return sum(stack)