class MinStack:

    # [1, 2, 0, 5]
    # [1, 1, 0, 0]

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        last = self.minStack[-1] if self.minStack else None
        if not self.minStack or val < last:
            self.minStack.append(val)
        else:
            self.minStack.append(last)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
