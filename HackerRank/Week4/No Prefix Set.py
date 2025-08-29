#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
def insert(trie, wrd):
    node = trie
    for i, ch in enumerate(wrd):
        if ch in node:
            if node[ch][1] or i == len(wrd) - 1:
                return True
        else:
            node[ch] = {}, (i == len(wrd) - 1)
        node = node[ch][0]
    return False

def noPrefix(words):
    trie = {}
    for wrd in words:
        if insert(trie, wrd):
            print("BAD SET")
            print(wrd)
            return
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
