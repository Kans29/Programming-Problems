#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for x in range(n)]
    for q in queries:
        a, b, k = q
        arr[a-1] += k
        arr[b] -= k
    value = x = 0
    for i in arr:
        x += i
        if x > value:
            value = x
    return value


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)