class MinStack:
    '''req:
        - O(1) time
    '''

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        ''' pushes val onto stack'''
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        '''removes element on top of stack'''
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        '''gets top elem of stack'''
        return self.stack[-1]

    def getMin(self) -> int:
        '''gets min element in stack'''
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
