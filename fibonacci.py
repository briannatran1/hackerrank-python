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


class Solution:
    def fib(self, n: int) -> int:
        '''req:
            - fn takes in an int
            - each num is the sum of the 2 preceding ones
            - starts at 0, 1

            iterative approach
        '''
        # edge cases: n = 0 or 1 --> return n
        # sum is of previous 2 nums (n - 1) + (n - 2)
        # initialize curr and prev vars --> reps 1st 2 fib nums
        # iterate through range of n + 1 starting at 2
        if n <= 1:
            return n
        
        prev = 0
        curr = 1

        for i in range(2, n + 1):
            # tuple assignment evaluates right hand side first
            # evaluates the right-hand side first, creating a tuple with the values (curr, prev + curr), 
            # and then assigns these values to prev and curr simultaneously. 
            # This means that prev gets the old value of curr, and curr gets the new value (the sum of the old prev and curr). 
            # This ensures that both updates happen at the same time without interfering with each other.
            prev, curr = curr, prev + curr
        
        return curr
