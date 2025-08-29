#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
MOD=1000000007
def legoBlocks(n, m):
    # Write your code here
    r = [0] * (m + 1)
    r[0] = 1
    for i in range(1, m + 1):
        for b in [1, 2, 3, 4]:
            if i - b >= 0:
                r[i] = (r[i] + r[i - b]) % MOD

    t = [pow(r[i], n, MOD) for i in range(m + 1)]

    s = [0] * (m + 1)
    s[0] = 1
    for i in range(1, m + 1):
        s[i] = t[i]
        for j in range(1, i):
            s[i] -= s[j] * t[i - j]
            s[i] %= MOD

    return s[m] % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
