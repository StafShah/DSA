class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max = maxSize
        self.currLen = 0
        
    def push(self, x: int) -> None:
        if self.currLen < self.max:
            self.stack.append(x)
            self.currLen += 1

    def pop(self) -> int:
        if self.currLen <= 0:
            return -1
        self.currLen -= 1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < self.currLen and i < k:
            self.stack[i] += val
            i += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)