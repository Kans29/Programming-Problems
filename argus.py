from sys import stdin
from heapq import *

def main():
	inp = stdin
	heap = []
	line = inp.readline().strip().split()
	while line[0] != '#':
		heappush(heap,[int(line[2]),int(line[1]),int(line[2])])
		line = inp.readline().strip().split()
	cant = inp.readline().strip()
	i = 0
	while i < int(cant):
		val = heappop(heap)
		print (val[1])
		val[0] = val[0] + val[2]
		heappush(heap,val)
		i+=1
main()