class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False


        stack = []
        
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif char == ')' and stack[-1] == '(':
                temp = stack.pop()
            elif char == '}' and stack[-1] == '{':
                temp = stack.pop()
            elif char == ']' and stack[-1] == '[':
                temp = stack.pop()
            else:
                stack.append(char)
        print(stack)
        return True if len(stack) == 0 else False
            