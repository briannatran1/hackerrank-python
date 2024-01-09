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
