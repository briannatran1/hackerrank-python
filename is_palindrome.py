class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''req: 
            - fn takes in a s
            - return true if palindrome
        '''
        # initialize 2 pointers
        # while left < right
        # if either char at each pos is not alphanumeric, increment/decrement respective pointer
        # if they're equal when they're lowercased, increment/decrement
        # else return False
        # return True after looping if else statement isn't reached
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
