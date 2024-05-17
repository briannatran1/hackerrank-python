class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # elem at mid is less than left neighbor, search left side
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            # elem at mid is less than right neighbor, search right side
            elif mid < right and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid # peak
        
        
