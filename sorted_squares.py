class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''req:
            - O(n) --> 2 pointer
            - fn takes in int arr in asc order
            - return sorted squares of each num in arr
        '''
        # initialize result list to size of nums filled with zeros
        # initialize left and right pointers
        # iterate over list in reverse
        # compare abs values of nums at pointers
        # if num at left > right, square left value and assign to curr idx of res,
        # increment left
        # else, assign right to idx in res and decrement right
        # return result list
        res = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range (len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1
        
        return res
