class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''req:
            - fn takes a str and integer
            - return length of longest substr w/ consec letters
        '''
        freq = {} # stores chars of curr window
        max_length = 0
        start = 0 # start idx of sliding window

        for end in range(len(s)):
            # updates freq of curr char
            freq[s[end]] = freq.get(s[end], 0) + 1 

            # calc length of curr window, then substract maximum frequency
            # see if this is <= k for validity
            curr_len = end - start + 1
            # record new max length if valid
            if curr_len - max(freq.values()) <= k:
                max_length = max(max_length, curr_len)
            # slide window
            else:
                freq[s[start]] -= 1
                start += 1
        
        return max_length
