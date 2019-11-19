'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema B - The Jackpot

Para solucionar este problema, se implemento el mismo principio que se uso al momento
de implementar Max Sum en clase, en el cual se usa como memoria adicional una variable
que guarda la maxima ganancia posible y siempre lo esta comparando con el valor actual.
'''

from sys import stdin
MAX = 610
bets = [ None for i in range(MAX) ]
def solve(cases):
	global bets
	ans,n,p,N = bets[0],1,bets[0],cases
	while n!=N:
		if p<=0:
			p = bets[n]
		else:
			p += bets[n]
			ans = max(ans,p)
		n+=1
	if ans <= 0:
		print('Losing streak.')
	else:
		print('The maximum winning streak is {0}.'.format(ans))

def main():
	global bets
	inp = stdin
	line = inp.readline().strip()
	while int(line) != 0:
		cases = int(line)
		bets = [int(x) for x in inp.readline().strip().split()]
		solve(cases)
		line = inp.readline().strip()
main()