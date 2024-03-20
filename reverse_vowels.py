class Solution:
    def reverseVowels(self, s: str) -> str:
        '''req:
            - reverse all vowels in str and return
        '''
        # initialize vowels var
        # turn str into list
        # 2 pointer method --> intialize left and right pointers
        # while left < right
        # if val at both positions are vowels, swap places & increment/decrement
        # if not, increment/decrement pointer
        # join list into str
        
        vowels = 'aeiouAEIOU'
        word = list(s)
        left = 0
        right = len(s) - 1

        while left <= right:
            if word[left] in vowels and word[right] in vowels:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            elif word[left] not in vowels:
                left += 1
            elif word[right] not in vowels: 
                right -= 1
        
        return ''.join(word)
