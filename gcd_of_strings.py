class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''req:
            - largest str should be unique (non-repeat)
        '''

        # check communicative property of strs for common divisor
        # if lengths of both strs are equal, then either str is the gcd
        # if len of str1 > str 2, recurse w/ substr of str1 after slicing premfix that matches str2
        # if len of str2 > str1, recurse w/ substr of str2 

        if str1 + str2 != str2 + str1: # no common divisor
            return ''
        
        if len(str1) == len(str2):
            return str1
        
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return self.gcdOfStrings(str1, str2[len(str1):])
