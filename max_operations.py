class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''req:
            - fn takes in int arr and int, k
            - remove only 2 elems from arr --> 1 operation
            - return max num of operations whose sum equal to k

            >>> nums = [1,2,3,4], k = 5
            2
            >>> nums = [1,2,3,4], k = 20
            0
        '''
        # sort arr in ascending order
        # initialize 2 pointers
        # initialize operations var to keep track
        # while left < right,
        # if elems at pointers is equal to k, increment operations and move pointers
        # if sum < k, increment left pointer
        # else sum > k, decrement right pointer
        # return operations
        nums.sort()

        left = 0
        right = len(nums) - 1
        operations = 0
        remaining_nums = []

        while left < right:
            if nums[left] + nums[right] == k:
                operations += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else: 
                remaining_nums.append(nums[right])
                right -= 1
        
        # add the remaining elements from the right pointer to the remaining_nums list
        while right >= left:
            remaining_nums.append(nums[right])
            right -= 1

        # replace the original nums list with the remaining elements
        nums[:] = remaining_nums
        
        return operations
        return operations
