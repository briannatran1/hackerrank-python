import sys

'''Programming challenge description:
    There is a board (matrix). Every cell of the board contains one integer,
    which is 0 initially.

    The following operations can be applied to the Query Board:
    SetRow i x: change all values in the cells on row "i" to value "x".
    SetCol j x: change all values in the cells on column "j" to value "x".
    QueryRow i: output the sum of values on row "i".
    QueryCol j: output the sum of values on column "j".

    The board's dimensions are 256x256.
    "i" and "j" are integers from 0 to 255.
    "x" is an integer from 0 to 31.
    Input:
    Your program should read lines from standard input. Each line contains
    one of the above operations.
    Output:
    For each query, output the result of the query.
    Test 1
    Test Input
    Download Test 1 Input

    >>> SetCol 32 20
        SetRow 15 7
        SetRow 16 31
        QueryCol 32
        SetCol 2 14
        QueryRow 10
    5118
    34
'''

# import numpy as np
# import pandas as pd
# from sklearn import ...

# create board
# iterate 256 times to create 256 rows
# create a new row w/ 260 zeros
# create fn for each operation
board = []

for _ in range(256):
    row = [0] * 256
    board.append(row)


def set_row(row, val):
    '''change all cells in specified row to given val'''
    # iterate through each col
    # set value of cell to given val
    for col in range(256):
        board[row][col] = val


def set_col(col, val):
    '''set all cells in col to given val'''
    # iterate through each row
    # set value of cell to val
    for row in range(256):
        board[row][col] = val


def query_row(row):
    '''return sum of all values in row'''
    # add all values in that row and return
    return sum(board[row])


def query_col(col):
    '''return sum of all values in col'''
    # intialize total_sum var
    # iterate through board
    # add row[col] to total_sum
    # return total_sum
    total_sum = 0

    for row in board:
        total_sum += row[col]

    return total_sum


for line in sys.stdin:
    inputs = line.split()
    operation = inputs[0]

    if operation == 'SetRow':
        row = int(inputs[1])
        val = int(inputs[2])
        set_row(row, val)
    elif operation == 'SetCol':
        col = int(inputs[1])
        val = int(inputs[2])
        set_col(col, val)
    elif operation == 'QueryRow':
        row = int(inputs[1])
        res = query_row(row)
        print(res)
    elif operation == 'QueryCol':
        col = int(inputs[1])
        res = query_col(col)
        print(res)
