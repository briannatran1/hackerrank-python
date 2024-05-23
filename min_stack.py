class MinStack:

    def __init__(self):
        # initialize a regular stack and a min_stack (for min elems)
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        '''pushes val onto stack'''
        # push val onto reg stack
        # if min_stack is not empty, assign val to lowest val of val or last val in min_stack
        # add val to min_stack
        self.stack.append(val)
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        
        self.min_stack.append(val)

        
    def pop(self) -> None:
        '''pops value from stack'''
        # pop off val from reg stack and min_stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        '''return top elem in reg stack'''
        # return last elem in stack
        return self.stack[-1]

    def getMin(self) -> int:
        '''returns min val in stack'''
        # return last elem in min_stack
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
