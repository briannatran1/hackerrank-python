class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''req:
            - return True if s is subsequence of t
            - else return False
            
            Subsequence --> 2 pointer?

            >>> s = 'abc', t = 'ahbgdc'
            True

            >>> s = 'axc' t = 'hiiii'
            False
        '''
        # initialize 2 pointers
        # while both pointers are less than the str lengths,
        # if letters are the same, increment i pointer
        # increment j no matter what
        # return true if i is at the end of s str
        # else, return false

        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
