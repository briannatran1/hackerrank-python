class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        '''req:
            - fn takes in arr of ints
            - returns bool

            >>> [1,2]
            false since 1 and 2 both occur 1 time

            >>> [1,2,2]
            true
        '''
        # create empty dict 
        # iterate through each num in arr and increment value of key when approached
        # return true if len of freq is equal to the len of freq values in a set
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        return len(freq) == len(set(freq.values()))
