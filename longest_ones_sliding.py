class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''req:
            - fn takes in binary arr and int
            - return max num of consec 1s if you can flip at most k 0's

            >>> [1,1,1,0,0,0,1,1,1,1,0], k = 2
            6

            >>> [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 0
            4

            >>> [], k = 2
            0
        '''
        # initalize left and right vars to 0
        left = right = 0

        for right in range(len(nums)):
            # if encounter a 0, decrement k
            if nums[right] == 0:
                k -= 1
            
            # if k < 0 increment left by 1 to slide window to remove extra 0s
            if k < 0:
                # if num at left is 0, increment k
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1
