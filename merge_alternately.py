class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''req:
            - start with word1 and add alternating letters
            - return merged str
        '''
        # edge cases: empty str
        # initialize merged var and pointers
        # while both words have length, add word1 letter first then word2
        # increment pointers
        # once a word is empty, add remaining letters
        # return merged str
        
        merged = ''
        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            merged += word1[i]
            merged += word2[j]
            i += 1
            j += 1

        merged += word1[i:]
        merged += word2[j:]
            
        return merged
