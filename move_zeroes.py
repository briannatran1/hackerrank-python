class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        >>> moveZeroes([0,1,0,3,12])
        [1,3,12,0,0]
        """
        # initialize pointer
        # iterate through arr
        # move non-zeros to front

        last_non_zero = 0
        n = len(nums)

        # moves all non-zero elems to front
        for i in range(n):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
