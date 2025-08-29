#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    arr = list(s)
    used = [False] * n
    i, j = 0, n - 1
    diff = 0

    while i < j:
        if arr[i] != arr[j]:
            diff += 1
        i += 1
        j -= 1

    if diff > k:
        return "-1"

    i, j = 0, n - 1
    remain = k
    while i < j:
        if arr[i] != arr[j]:
            bigger = max(arr[i], arr[j])
            arr[i] = arr[j] = bigger
            used[i] = used[j] = True
            remain -= 1
        i += 1
        j -= 1

    i, j = 0, n - 1
    while i < j and remain > 0:
        if arr[i] != '9':
            cost = 1 if (used[i] or used[j]) else 2
            if remain >= cost:
                arr[i] = arr[j] = '9'
                remain -= cost
        i += 1
        j -= 1

    if n % 2 == 1 and remain > 0:
        arr[n // 2] = '9'

    return "".join(arr)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')
    fptr.close()
