#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    if n==1:
        return grid
    row , col = len(grid) , len(grid[0])
    if n% 2==0:
        return ["O" * col for _ in range(row)]
    def blast(a):
        blasted = [list("O" * col) for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if a[r][c] == 'O':
                    blasted[r][c]= '.'
                    if r > 0:
                        blasted[r-1][c] = '.'
                    if r+1 < row:
                        blasted[r+1][c] = '.'
                    if c>0:
                        blasted[r][c-1] = '.'
                    if c+1 < col:
                        blasted[r][c+1] = '.'
        return ["".join(row) for row in blasted]
    grid_first = blast(grid)
    grid_second = blast(grid_first)
    
    if n % 4==3:
        return grid_first
    else:
        return grid_second
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
