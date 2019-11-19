#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    Q = [x-1 for x in arr]
    i,swaps = 0,0
    while i < len(Q):
    	while Q[i] != i:
    		temp = Q[Q[i]]
    		Q[Q[i]] = Q[i]
    		Q[i] = temp
    		swaps +=1
    	i+=1
    return swaps

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)