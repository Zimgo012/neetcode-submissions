class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # print(self.stack, "stack")
        if not self.minstack:
            self.minstack.append(val)
        else:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        # print(self.minstack, "minstack")

    def pop(self) -> None:        
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()

        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
