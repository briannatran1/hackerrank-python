class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''req:
            - fn takes arr of ints and extraCandies(int)
            - multiple kids can have greatest num of candies
            - return bool arr which indicates if kid is given extraCandies, 
            they will have the most candies
        '''

        # initialize result arr var
        # initialize max_candies var
        # iterate through candies
        # after adding extraCandies, compare to max
        # if greater, push true to arr
        # else, push false

        max_candies = max(candies)
        result = list()

        for candy in candies:
            if (candy + extraCandies) >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
