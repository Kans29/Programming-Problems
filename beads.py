from sys import stdin
MAX = 100010
T =""
n =0
RA = [0 for x in range(MAX)]
tempRA = [0 for x in range(MAX)]
SA = [0 for x in range(MAX)]
tempSA = [0 for x in range(MAX)]
c = [0 for x in range(MAX)]

def countingSort(k):
	global T,n,RA,SA,tempRA,tempSA,c
	maxi = max(300, n)
	c = [0 for x in c]
	i = 0
	while i < n:
		if i + k < n:
			c[RA[i + k]]+=1
		else: 
			c[0]+=1
		i+=1
	i,suma = 0,0
	while i < maxi:
		t = c[i]
		c[i] = suma
		suma += t
		i+=1
	i = 0
	while i < n:
		if SA[i]+k < n:
			tempSA[c[RA[SA[i]+k]]] = SA[i]
			c[RA[SA[i]+k]]+=1
		else:
			tempSA[c[0]] = SA[i]
			c[0]+=1
		i+=1
	i = 0
	while i < n:
		SA[i] = tempSA[i]
		i+=1

def constructSA(): 
	global T,n,RA,SA,tempRA,tempSA,c
	i = 0
	while i < n:
		RA[i] = ord(T[i])
		i+=1
	i = 0
	while i < n:
		SA[i] = i
		i+=1 
	k,r = 1,0
	while k < n: 
		countingSort(k)
		countingSort(0) 
		tempRA[SA[0]] = r = 0
		i = 1
		while i < n:
			if (RA[SA[i]] == RA[SA[i-1]] and RA[SA[i]+k] == RA[SA[i-1]+k]):
				tempRA[SA[i]] = r 
			else:
				r+=1
				tempRA[SA[i]] = r 
			i+=1
		i = 0
		while i < n:
			RA[i] = tempRA[i]
			i+=1
		if RA[SA[n-1]] == n-1: 
			break
		k <<= 1

def solve(): 
	global T,n,RA,SA,tempRA,tempSA,c
	N = len(T)
	T+= T+'~'
	n = len(T)
	constructSA();
	i = 0
	while i < n:
		if len(T[SA[i]:n]) >= N:
			return SA[i]+1
		i+=1
def main(): 
	global T,n,RA,SA,tempRA,tempSA,c
	inp = stdin
	cases = int(inp.readline().strip())
	i = 0
	while i < cases:
		T = inp.readline().strip()
		print(solve())
		i+=1
main()