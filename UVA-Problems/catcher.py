'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema C - Testing the CATCHER

En este problema se implementó programacion dinamica a traves del metodo de tabulación
La estructura usada para este problema se basa en una lista del mismo tamaño
que la lista de entrada de los disparos, para llenarla, se usa el criterio de la mejor de las
opciones que se consiguien a partir del misil catch[n] y se guarda en possibility[n], teniendo
al final en la lista todas las mejores opciones, de la cual se esoge el maximo.
'''
from sys import stdin

def solve(catch):
	n = 1
	N = len(catch)
	possibility = [0 for x in range(N)]
	possibility[0] = 1
	while n!=N:
		j = 0
		maxim = 0
		while j != n+1:
			if(catch[j] >= catch[n] and possibility[j]+1 > maxim):
				maxim = possibility[j]+1
			else:
				j+=1
		possibility[n] = maxim
		n +=1
	return max(possibility)

def main():
	inp = stdin
	bandera = True
	cases = 1
	catch = []
	while bandera == True:
		line = int(inp.readline().strip())
		if line == -1:
			line = int(inp.readline().strip())
			ans = solve(catch)
			catch = []
			if line == -1:
				bandera = False
				print ('Test #{0}:'.format(cases))
				print ('  maximum possible interceptions: {0}'.format(ans)) 
			else:
				print ('Test #{0}:'.format(cases))
				print ('  maximum possible interceptions: {0}\n'.format(ans)) 
				cases += 1
				catch.append(line)
		else:
			catch.append(line)
main()