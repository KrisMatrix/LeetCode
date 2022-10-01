class MyQueue:
    # Remembe: You must use a stack. Stacks are LIFO. So you can only
    # use append(val) and pop(). The pop may not accept paramenters.
    # i.e. you cannot do pop(0)

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.queue) == 0:
            while (len(self.stack) > 0):
                self.queue.append(self.stack.pop())
        return self.queue.pop()
        
            
    def peek(self) -> int:
        if len(self.queue) == 0:
            while (len(self.stack) > 0):
                self.queue.append(self.stack.pop())
        return self.queue[len(self.queue) - 1]

    def empty(self) -> bool:
        if (len(self.queue) == 0) and (len(self.stack) == 0):
            return True
        else:
            False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
