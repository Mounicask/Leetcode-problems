class MinStack:

    def __init__(self):
        self.list_a = []
        

    def push(self, x: int) -> None:
        self.list_a.append(x)

    def pop(self) -> None:
        return self.list_a.pop()

    def top(self) -> int:
        top = len(self.list_a) - 1
        return self.list_a[top]

    def getMin(self) -> int:
        if len(self.list_a)!=0:
            min_ele = min(self.list_a)
            return min_ele 


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
obj.getMin()
obj.pop()
obj.getMin()
obj.pop()
obj.getMin()
obj.pop()
obj.getMin()


