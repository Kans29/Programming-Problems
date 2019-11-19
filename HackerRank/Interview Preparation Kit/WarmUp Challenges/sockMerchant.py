from sys import stdin

def main():
    N ,ans = int(stdin.readline().strip()),0
    socks = [int(x) for x in stdin.readline().strip().split()]
    socks.sort()
    i,j = 0,1
    if N > 1:
        while i < N and j < N:
            if socks[i] == socks[j]:
                ans+=1
                i,j = i+2,j+2
            else:
                i,j = i+1,j+1
    print(ans)
main()  