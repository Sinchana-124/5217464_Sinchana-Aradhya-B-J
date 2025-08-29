#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    def no_of_swaps(a):
        indexmap = {a[i]: i for i in range(len(a))}
        sorted_arr = sorted(a)
        result = 0
        for i in range(len(a)):
            if a[i] != sorted_arr[i]:
                result += 1
                swap_index = indexmap[sorted_arr[i]]
                indexmap[a[i]] = swap_index
                indexmap[sorted_arr[i]] = i
                a[i], a[swap_index] = a[swap_index], a[i]
        return result

    normal_order = no_of_swaps(arr[:])
    reverse_order = no_of_swaps(arr[::-1])
    return min(normal_order, reverse_order)

     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
