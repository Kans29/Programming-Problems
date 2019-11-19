#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    names = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if len(re.findall('[a-z]+@gmail\.com',emailID)) != 0:
        	names.append(firstName)
    names.sort()
    for i in names:
    	print(i)


