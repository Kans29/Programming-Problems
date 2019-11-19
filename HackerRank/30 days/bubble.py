#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
i,globalSwaps = 0,0
while i < n:
    numberOfSwaps = 0
    j = 0
    while j < n-1:
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numberOfSwaps+=1
        
        j+=1
    
    globalSwaps+=numberOfSwaps
    i+=1

print('Array is sorted in {0} swaps.'.format(globalSwaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[n-1]))