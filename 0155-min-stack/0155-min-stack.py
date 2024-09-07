class MinStack:

    def __init__(self):
        self.info = []
        self.min = 2**31

    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.info.append((val, self.min))

    def pop(self) -> None:
        self.info.pop()
        if len(self.info) > 0:
            self.min = self.info[-1][1]
        else:
            self.min = 2**31

    def top(self) -> int:
        if len(self.info) > 0:
            return self.info[-1][0]
        else:
            return None

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()