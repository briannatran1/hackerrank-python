class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' req: 
            - fn takes arr of ints and an integer, k
            - return k most freq elems in any order
        '''
        result = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # sorting will be based on key value frequencies
        # done in descending order
        sorted_freq = sorted(freq, key=freq.get, reverse=True)
        #returns slice of list of first k elems
        return sorted_freq[:k]

# create dict to store freq
# iterate and update num count in dict
