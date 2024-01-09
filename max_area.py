class Solution:
    def maxArea(self, height: List[int]) -> int:
        ''' req:
            - fn takes an int arr
            - return max amount of water container can store bwt 2 lines
            - cannot slant container
        '''
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area


# initialize 2 pointers
# declare max_area
# iterate while left is less than right
# calculate curr area
# update max area
# move pointers inward according to each height
# return max area
