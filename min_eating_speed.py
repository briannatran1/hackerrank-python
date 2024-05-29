class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''req:
            - pile < k bananas --> eats all of them and not anymore for that hour
            - return min int
        '''
        # use binary search on range [1, max(piles)] to identify the optimal 
        # eating speed
        # enter binary search while loop
        # initialize total_hours var
        # iterate through piles
        # calculate total hours required to eat all the bananas at the current speed mid
        # if total_hours <= h, koko can finish eating at this speed or lower, find the min
        # move right boundary towards smaller half
        # else, koko needs to eat faster, move left boundary to larger half
        # return res
        
        left = 1 #least amount of bananas eaten
        right = max(piles) # most bananas eaten
        res = right

        while left <= right:
            mid = (right + left) // 2
            total_hours = 0

            for p in piles:
                total_hours += math.ceil(p / mid)

            if total_hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res
