class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''req:
            - fn takes in arr of ints (1-indexed) & target int
            - return indices of 2 elems that add up to target sum (guaranteed)
        '''
        start = 0
        end = len(numbers) - 1

        while start < end:
            sum = numbers[start] + numbers[end]

            if sum == target:
                return [start + 1, end + 1]
            elif sum < target:
                start += 1
            else:
                end -= 1

# 2 pointer method
# initialize start and end pointers
# while start pointer is less than end pointer,
# initialize sum var w/ nums at both pointers
# if sum is equal to target, return indices + 1
# if sum < target, increment start
# else, decrement end
