class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' req: 
            - fn takes a str of letters
            - return length of longest substr w/o dupes
        '''
        n = len(s)
        if n == 0:
            return 0
        
        indices = {}
        start = 0
        max_length = 0

        for end in range(n):
            if s[end] in indices and indices[s[end]] >= start:
                start = indices[s[end]] + 1
            
            indices[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length

# use sliding window approach
# if s is empty, return 0
# create dict for char indices
# declare start pointer
# declare max length var
# iterate through range of input s
# if there is a dupe, adjust start to the right
# update indices w/ current char index(end)
# update max_length to largest length
# return max_length
