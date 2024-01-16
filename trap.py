class Solution:
    def trap(self, height: List[int]) -> int:
        '''req:
            - fn takes arr of non-neg ints
            - return num (trapped rain water)
        '''
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
        
        return water

# 2 pointer method
# initialize left and right pointers
# initialize max heights for each side and water vars
# while left pointer < right
# update max heights with each iteration
# if left max height < right max height,
# calculate trapped water and incrememnt left
# else do right side
# return trapped water
