class Solution:
    def compress(self, chars: List[str]) -> int:
        '''req:
            - O(1) space complexity
            - return len of arr only

            >>> chars = ["a","a","b","b","c","c","c"]
            6 (compressed str: 'a2b2c3' stored in arr)
        '''
        # initialize ans var and i pointer
        # if arr len is 1, return 1
        # iterate through chars from idx 1
        # compare curr elem with prev elem
        # if they are the same, increment count
        # 
        # return len of arr
        ans = 0 # keep track of the index where characters will be stored after compression.
        i = 0
        n = len(chars)

        if n == 1:
            return 1
        
        while i < n:
            letter = chars[i] # curr char
            count = 0 # counts consec occurrences of letter

            while i < n and chars[i] == letter: # consec letter
                count += 1
                i += 1
            
            chars[ans] = letter # store letter in chars arr at idx ans
            ans += 1

            if count > 1:
                for c in str(count): # turns count into str
                    chars[ans] = c # adds each digit to chars at idx ans
                    ans += 1
        
        return ans # len of compressed str
