class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0

        while left <= right:
            mid = (right + left) // 2

            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
        
        return ans

# binary search

# find left and right sides
# set ans to 0
# while left does not overlap right side,
# find mid point
# if mid^2 > x, search left side
# else search right side and set ans to mid
# return ans
