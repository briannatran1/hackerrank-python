class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''req:
            - fn takes in arr of integers
            - return true if dupe exists
            - return false if each val is unique
        '''
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for val in count.values():
            if val != 1:
                return True
        
        return False

# create counter 
# iterate through list and update count for each num
# iterate through counter values
# if val does not equal 1, return true
