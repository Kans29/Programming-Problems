from sys import stdin
from heapq import *

def solve(numeros):
	cost = 0
	heapify(numeros)
	while len(numeros) != 1:
		val1 = heappop(numeros)
		val2 = heappop(numeros)
		heappush(numeros,val1+val2)
		cost += val1+val2
	print(cost)

def main():
	inp = stdin
	N = int(inp.readline().strip())
	while N!= 0:
		numbers = [int(x) for x in inp.readline().strip().split()]
		solve(numbers)
		N = int(inp.readline().strip())
main()