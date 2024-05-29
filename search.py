class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''req:
            - fn takes in arr of ints in ascending order and a target int
            - return index if target exists in arr
            - else, return -1
        '''
        # initialize left and right pointers
        # while left < right, enter a loop
        # find mid point of nums
        # if num at mid == target, return mid
        # elif num at mid < target, search right side
        # else, search left side
        # return -1 if target is not found
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1 
