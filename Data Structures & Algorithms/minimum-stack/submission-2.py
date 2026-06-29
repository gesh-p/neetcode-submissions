class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.min) == 0:
            self.min.append(val)

        if self.min[-1] >= val:
            self.min.append(val)
        
    def pop(self) -> None:
        temp = self.stack.pop()

        if self.min[-1] == temp:
            min_temp = self.min.pop()
            
        if len(self.stack) == 0:
            self.min = []

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min) == 0:
            return None

        return self.min[-1]
        
