class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''req:
            - fn takes a str and int
            - return max num of vowels in a substring w/ length k

            >>> s = "abciiidef", k = 3
            3

            >>> s = "tttt", k = 3
            0
        '''
        # initialize vowels var
        # initialize count and ans var
        vowels = 'aeiou'
        ans = count = 0

        # count vowels in first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        ans = max(ans, count)

        # slide window and update count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            ans = max(ans, count)

        return ans
