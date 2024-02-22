class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # no rotation
        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
        

#initialize 2 pointers for binary search (left and right)
#initialize var for lowest --> default to 1st elem
#if elem at left is less than elem at right, arr is not rotated -> min is at left
#while loop until left exceeds right
#find mid point 
#if num at mid is greater than last elem, rotation occurs to the right of mid
#therefore, min elem is in right half of arr, update left
#else min is in left half of arr, update right
