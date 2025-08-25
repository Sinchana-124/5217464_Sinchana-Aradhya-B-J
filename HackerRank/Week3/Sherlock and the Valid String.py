#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    from collections import Counter
    wave = Counter(s)
    variables = list(wave.values())
    wave_count = Counter(variables)
    if len (wave_count)==1:
        return "YES"
    elif len (wave_count) ==2:
        (f1, c1), (f2 , c2) = Counter(wave_count).items()
        if (f1==1 and c1== 1) or ( f2 ==1 and c2==1):
            return "YES" 
        if (abs(f1 - f2)==1) and ((c1 == 1)or (c2 ==1)):
            return "YES"    
        return "NO"
    else:
        return "NO"         
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
