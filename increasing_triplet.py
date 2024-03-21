class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''req: 
            - return bool if i < j < k and nums[i] < nums[j] < nums[k]
        '''
        # initialize 2 vars to infinity
        # iterate through num
        # if n <= i, reassign i as n
        # elif n <= j, reassign j as n
        # else return True
        # return False

        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        
        return False
