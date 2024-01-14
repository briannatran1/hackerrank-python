class Solution:
    def isValid(self, s: str) -> bool:
        ''' req: 
            - fn takes in a str
            - return boolean for certain conditional
        '''
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
        
        return len(stack) == 0 

# create a stack (append and pop)
# create a dict of matching pairs
# loop through each char in s
# if it's a valid bracket, add to stack
# else if there are no more brackets to correspond to, or popped bracket doesn't match,
# return False
# return true if stack is empty after looping
