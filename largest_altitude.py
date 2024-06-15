class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''req:
            - inputs: int arr
            - output: int

            gain[i] -> sum of points i and i + 1
        '''
        # init max and curr alt vars to 0
        # iterate over gain arr
        # add curr gain to curr_alt at each iteration
        # update max_alt to the highest of the 2 vars
        # return max_alt
        max_alt = 0
        curr_alt = 0

        for g in gain:
            curr_alt += g
            max_alt = max(max_alt, curr_alt)
        
        return max_alt
