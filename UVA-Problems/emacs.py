"""
Algoritmo Knuth-Morris-Pratt para busqueda de una cadena adentro de otra
complejidad temporal/espacial  = O(n+m) / O(n)
"""

from sys import stdin

def arrayBuild(P):
	N = len(P)
	A = [0 for x in range(N)]
	i,j = 1,0
	while i < N:
		if P[i] == P[j] or P[i] == '*' or P[j] == '*':
			j=j+1
			A[i] = j
			i+=1
		else:
			if j != 0:
				j = A[j-1]
			else:
				A[i] = j
				i+=1
	if N >= 2:
		if P[N-2] == '*': A[N-1] = N-1
	return A
def patternSearch(A,B):
	M = len(A)
	B = B.strip('*')
	N = len(B)
	array = arrayBuild(B)
	i,j,ans = 0,0, "yes"
	while j < N and i < M:
		if A[i] == B[j]:
			i,j=i+1,j+1
		else:
			if B[j] == '*':
				j+=1
			elif j != 0 and B[j-1] != '*':
				j = array[j-1]
			else:
				i +=1
	if j != N:
		ans = "no"
	return ans

def main():
	inp = stdin
	N = inp.readline().strip()
	while len(N)>0:
		cases = int(N)
		word = inp.readline().strip()
		while cases > 0:
			search = inp.readline().strip()
			print(patternSearch(word,search))
			cases -=1
		N = inp.readline().strip()
main()