class MinStack:

    def __init__(self):
        self.A = [float('inf')]
        self.min = [float('inf')]

    def push(self, x: int) -> None:
        self.A.append(x)
        self.min.append(min(x,self.min[-1]))

    def pop(self) -> None:
        self.A.pop()
        self.min.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.min[-1]