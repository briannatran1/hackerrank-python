class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''req:
            - O(log n) time
            - fn takes sorted arr of ints, target int
            - return index if target can be found
            - otherwise, return -1
        '''
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = math.floor((right + left) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
        
        return -1

# find left and right sides of arr
# loop until left meets right
# find mid point
# if num at mid is target, return true
# else if num at mid < target, search right side 
# else search left side
# return -1 if no target found
