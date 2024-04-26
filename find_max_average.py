class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''req:
            - 5 decimal places
            - fn takes int arr and int, k
            - return max average of subarr whose length = k
            
            continguous subarray --> sliding window approach

            >>> nums = [1,12,-5,-6,50,3], k = 4
            12.75000

            >>> nums = [5], k = 1
            5.00000
        '''
        # initialize curr_sum and max_sum to sum of initial k elems
        
        curr_sum = max_sum = sum(nums[:k])

        # iterate from kth elem
        # subtract left elem of window
        # add right elem of window
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]

            # update max
            max_sum = max(max_sum, curr_sum)
        
        # return avg
        return max_sum / k
