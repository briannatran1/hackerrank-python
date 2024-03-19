class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''req:
            - cannot be planted in adjacent plots
            - fn takes in arr of 1s and 0s and n (int)
        '''
        # if n is 0 --> return True since no flowers need to be planted
        # iterate through flowerbed
        # if curr plot is 0, and curr plot is the first plot or the prev plot is empty,
        # and if the curr plot is the last plot or the next plot is empty, 
        # plant flower
        # decrement n
        # if there are no flowers left to plant, return False
        # return False

        size = len(flowerbed)

        if n == 0:
            return True

        for i in range(size): 
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True
        
        return False
