class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''req:
            - fn takes in a grid/matrix
            - find min path from top left to bottom right
        '''
        # create vars for len of row and col
        # iterate over each row starting from the 2nd row
        # calculate path sum vertically
        # iterate over each col starting from the 2nd col
        # calculate path sum horizontally
        # iterate over rest of cells using nested loop
        # add min val of cell directly above and to the left
        # return value of bottom right cell

        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]
