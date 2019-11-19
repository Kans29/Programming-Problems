#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    moves = 0 
    Q = [P-1 for P in q]
    for i,P in enumerate(Q):
        if P - i > 2:
            return "Too chaotic"
        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    return moves

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
