class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''req:
            - fn takes in arr of ints
            - return arr of leftover asteroids

            >>> asteroids = [5,10,-5]
            [5, 10]

            >>> asteroids = [8,-8]
            []

            Time: O(n)
        '''
        # initialize a stack
        # iterate through asteroids
        # calculate sum of current asteroid and top of stack
        # 2 outcomes --> collision or no collision
        # collision only happens when num in stack > 0 and when asteroid < 0
        # if collision occurs, and num in stack is less than curr num, pop from stack
        # then compare curr num to next in stack
        stack = [] # [5, 10, -5]
        for a in asteroids:  # 5 # 10 # -5
            while stack and stack[-1] > 0 and a < 0: # stack [5, 10], 10 > 0, -5 < 0
                diff = a + stack[-1] # -5 + 10 = 5
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else: # both are destroyed
                    a = 0
                    stack.pop()
    
            if a:     
                stack.append(a) # [5, 10]

        return stack # [5, 10]
