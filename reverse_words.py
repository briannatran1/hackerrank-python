class Solution:
    def reverseWords(self, s: str) -> str:
        '''req:
            - trim any extra spaces
            - return str of words in reverse order
        '''
        # split str into words list and filter out empty strs
        # reverse words and join with spaces
        # return 

        words = [word for word in s.split() if word]
        
        reversed_word = ' '.join(words[::-1])
        
        return reversed_word
