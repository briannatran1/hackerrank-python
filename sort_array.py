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

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''requirements:
            - fn takes in list of ints
            - do not use built-in fns
            - O(n log(n)) time 
            - return arr in ascending order
        '''
        n = len(nums)
        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


# bubble sort:
# iterate through arr used nested loops and swap numbers if necessary
# largest number will keep going towards end of arr

# iterate through nums using nested loops
# if curr is greater than next,
# swap elems

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''requirements:
            - fn takes in list of ints
            - do not use built-in fns
            - O(n log(n)) time 
            - return arr in ascending order
        '''
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        
        return nums

# selection sort:
# find min elem and swap w unsorted elem

# iterate through nums using nested loops
# outer loop iterates through each element in the list
# find index of min val
# inner loop starts from the next element after the current one (i + 1) and goes until the end of the list.
# if first elem is greater than min, update min index to smaller one
# swap min w current elem
# return list
