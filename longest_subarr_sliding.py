class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''req:
            - fn takes in binary arr
            - return longest subarr containing only 1s after deleting one element

            >>> [1, 1, 0, 1]
            3

            >>> [0, 0, 0]
            0
        '''
        # initialize left pointer, zeros var, and ans var 
        # iterate over arr using right pointer
        # if num at right pos is 0, increment count of zeros
        left = 0
        zeros = 0
        ans = 0 # holds len of longest subarr

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            # adjust window to maintain at most 1 zero in subarr
            # by moving left pointer to the right when encountering a zero
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # updates max subarr
            ans = max(ans, right - left)

        return ans
