class Solution:
    def removeStars(self, s: str) -> str:
        '''req:
            - fn takes in a str
            - return str after removing *

            >>> s = "leet**cod*e"
            "lecoe"

            >>> s = "erase*****"
            ""
        '''
        # initialize a stack to store letters
        # iterate through s
        # if char is a letter, push to stack
        # else, char is a star --> want pop off to char from stack to remove
        # return stack joined into a str
        stack = []

        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                stack.pop()
        
        return ''.join(stack)
