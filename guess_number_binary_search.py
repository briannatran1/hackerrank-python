# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
 

class Solution:
    def guessNumber(self, n: int) -> int:
        '''req: 
            - 
            - 
        '''
        # initialize first to 1 and last to n
        # while first <= last,
            # calculate mid
            # if guess(mid) returns 0, return mid
            # if guess(mid) returns -1, update last to mid - 1
            # if guess(mid) return 1, update first to mid + 1
        # return -1
        first = 1
        last = n

        while first <= last:
            mid = (first + last) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                last = mid - 1
            else:
                first = mid + 1
        
        return -1
