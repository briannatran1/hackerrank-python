class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''req:
            - inputs: nums arr
            - output: num (pivot idx of arr -- leftmost)

            pivot idx = where sum of numbers on left is equal to numbers on right
        '''
        # init total to sum of nums
        # init left_total to 0
        # iterate through nums
        # calc right_total by subtracting total, left_total, and curr num
        # if right_total is equal to left_total
        # return index
        # else, add num to left_total
        # return -1 if no pivot is found
        total = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total - nums[i]

            if right_total == left_total:
                return i
            else:
                left_total += nums[i]
        
        return -1
