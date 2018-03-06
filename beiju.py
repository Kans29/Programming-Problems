from sys import stdin
from collections import deque

def solve(frase):
	resultado = deque()
	back = deque()
	bandera = False
	for i in frase:
		if i == '[':
			bandera = True
			resultado.extendleft(back)
			back = deque()
		elif i == ']':
			resultado.extendleft(back)
			back = deque()
			bandera = False
		else:
			if bandera == False:
				resultado.append(i)
			else:
				back.extendleft(i)
	resultado.extendleft(back)
	ans = []
	for i in resultado:
		ans.append(i) 
	print (''.join(ans))

def main():
	inp = stdin
	line = inp.readline().strip()
	while len(line) > 0:
		solve(line)
		line = inp.readline().strip()
main()