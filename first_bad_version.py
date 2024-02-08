# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        version = 1

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
                version = mid
        
        return version

# use binary search
# find left and right sides of n
# set version to 1
# while left and right are not overlapping, 
# find mid point
# if version at mid point is false, check right side
# else check left side
# return version num
