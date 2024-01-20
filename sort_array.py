class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''requirements:
            - fn takes in list of ints
            - do not use built-in fns
            - O(n log(n)) time 
            - return arr in ascending order
        '''
        n = len(nums)
        for i in range(1, n):
            curr = nums[i]
            j = i - 1 

            while j >= 0 and nums[j] > curr:
                nums[j + 1] = nums[j] # shifts larger elem to right
                j -= 1
            nums[j + 1] = curr

        return nums

# insertion sort:
# compare curr and prev elems and switch if curr is less than prev

# initialize var for length of nums list
# loop through nums starting at 2nd elem
# initalize j var to i - 1 for prev elem
# while curr num can still be swapped (prev > curr)
# shift larger elem to right til correctly placed
# decrement j
# assign value of curr to next index
