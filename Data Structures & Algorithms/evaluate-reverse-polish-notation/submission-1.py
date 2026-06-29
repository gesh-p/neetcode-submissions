class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        n = len(tokens)
        stack = []
        operands = {'+', '-', '*', '/'}

        for i, token in enumerate(tokens):
            if token not in operands:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()

                if token == '+':
                    curr = x + y
                elif token == '-':
                    curr = x - y
                elif token == '*':
                    curr = x * y
                else:
                    curr = x // y
                    if curr < 0 and x / y != x // y:
                        curr += 1
                
                stack.append(curr)

        return stack[0]



