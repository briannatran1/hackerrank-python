class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''req:
            - fn takes in int matrix m x n and int target
            - each row is in ascending order
            - 1st cell in row is greater than last cell in prev row
            - return true if target is in matrix
            - false if not
            - O(log(m * n)) time complexity --> binary search

            >>> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
            true

            >>> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
            false
        '''
        # get rows and cols
        # initialize top and bot pointers
        # while top <= bot, calculate mid row/arr to look in 
        # check if target val is larger than the last value in the mid row
        # set top/bot accordingly
        # do binary search within correct row
        
        rows, cols = len(matrix), len(matrix[0])
        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else: # target in row so break out of loop
                break
        
        if not top <= bot:
            return False

        row = (top + bot) // 2
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        
        return False
