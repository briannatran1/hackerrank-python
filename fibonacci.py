class Solution:
    def fib(self, n: int) -> int:
        '''req:
            - fn takes in an int
            - each num is the sum of the 2 preceding ones
            - starts at 0, 1
        '''
        # base case: n = 0 or 1 --> return n
        # sum is of previous 2 nums (n - 1) + (n - 2)
        # recursively call fn for 2 prev nums and return sum
        if n <= 1:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)
