#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        s = range(1,n+1)
        if n>=k|(k-1):
            minim = k-1
        else:
            minim = k-2.
        print(int(minim))