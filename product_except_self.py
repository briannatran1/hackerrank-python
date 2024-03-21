class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' req: 
            - fn takes arr of integers
            - return arr of products that excludes curr val
            - O(n) time 
        '''
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        # stores products
        result = [0] * n 

        # calculates product of elems to left of curr num
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        
        # calculates product of elems to right of curr num
        for i in range(n - 1, -1, -1):
            result[i] *= postfix_product
            postfix_product *= nums[i]

        return result

# 2nd solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' req: 
            - fn takes arr of integers
            - return arr of products that excludes curr val
            - O(n) time 
        '''
        # create 2 arrs, prefix and suffix, both initialized w/ ones and having 
        # the same length as nums.. will hold products of elements 
        # calculate product to the left of curr val
        # calculate product to the right of curr val
        # multiple each prefix and suffix prod for each index to get result
        # return result

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # loops starts at 1 and goes up to n - 1
        for i in range(1,n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # loop starts from 2nd to last index and goes backward down to 0
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        result = [prefix[i] * suffix[i] for i in range(n)]

        return result
