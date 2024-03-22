class Solution:
    def maxArea(self, height: List[int]) -> int:
        ''' req:
            - fn takes an int arr
            - return max amount of water container can store bwt 2 lines
            - cannot slant container

            >>> maxArea([1,8,6,2,5,4,8,3,7])
            49

            >>> maxArea([1,1])
            1
        '''
        # initialize 2 pointers
        # declare max_area -- keeps track of max area encountered
        # iterate while left is less than right
        # calculate curr area: find min height bwt left and right pointers,
        # multiple min height by width --> area
        # update max area if curr area > max area
        # move pointers inward according to each height
        # return max area
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)

            # finding tallest bar
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area

