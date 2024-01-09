class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''req: 
            - fn takes an arr of integers and a target int
            - return indices of 2 numbers that add up to target
            - only 1 solution
        '''
        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
        
        return []


# create dict to store to store nums in arr w/ their indices
# iterate through each elem in arr
# calculate complement for each elem
# if complement is in dict, return indicies
# else, add key to index value
# return empty list if no solution
