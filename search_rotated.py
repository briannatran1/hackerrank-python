class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            #right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

#initialize 2 pointers for binary search (left and right)
#while loop until left exceeds right
#find mid point 
#if num at mid is the target, return mid
#if left half is sorted (num at left is <= num at mid)
    #if target is in between num at left and mid, search left half
    #else, search right half
#if right half is sorted,
    #if target is greater than elem at mid and less than elem at right, search right half
    #else, search left half
# return -1 if target not found
