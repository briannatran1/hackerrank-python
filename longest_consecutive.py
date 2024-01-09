class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''req:
            - fn takes unsorted arr of ints
            - return length of longest consec elems
            - O(n) time
        ''' 
        longest = 0
        # efficient for membership checks
        num_set = set(nums)

        while num_set:
            low = high = num_set.pop()

            while low - 1 in num_set or high + 1 in num_set:
                # checking for lower num than curr val
                if low - 1 in num_set:
                    num_set.remove(low - 1)
                    low -= 1
                # checking for higher num than curr val
                if high + 1 in num_set:
                    num_set.remove(high + 1)
                    high += 1
            
            longest = max(high - low + 1, longest)
        
        return longest

# convert list to set
# iterate while num_set is not empty
# create low and high vars and assign to curr popped val
