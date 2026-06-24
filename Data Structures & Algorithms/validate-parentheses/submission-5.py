class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        opening = {'(', '[', '{'}
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) != 0 and dic[char] == stack[-1]:
                    temp = stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False
            