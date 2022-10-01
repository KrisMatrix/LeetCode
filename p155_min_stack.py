class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.min) == 0:
            self.min.append(val)
        elif val < self.min[0]:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if len(self.min) > 0:
            minval = self.min.pop()
        else:
            minval = None
        if minval == popped:
            self.min.pop()
        elif minval != None:
            self.min.append(minval)
        return popped

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        #return min(self.stack)
        if len(self.min) == 0:
            return
        else:
            return self.min.pop()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
