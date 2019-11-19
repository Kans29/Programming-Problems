'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema B - Forests

Para este problema, se aplico la teoria de conjuntos disjuntos, en el cual cada conjunto es el
agrupamiento entre personas i arboles, en donde se maneja que la persona i escucho el arbol j.
Inicialmente, se organiza la entrada en un diccionario, de modo que al revisar dict[i] = j..jn
mostrando todos los arboles de la persona i, siendo esta su opinion.
El representante de cada conjunto sera el conjunto de arboles escuchados por las personas, teniendo
que conjunto [1,2] como representante, indicaria todas las personas que escucharon solamente los
arboles 1 y 2.
De este modo, cada conjunto disjunto seria una opinion distinta, puesto que la gente que solo escucho
el arbol 1 tiene una opinion distinta que los que escucharon el arbol 1 y el 2.
Se procede a unir los conjuntos que posean los mismos elementos, y al final se tiene una lista con todos
los conjuntos disjuntos, de la cual se retorna el largo total, siendo estas las opiniones.
'''
from sys import stdin

def solve(personas,arboles,opiniones):
	for i in range(1,personas):
		for j in range(i+1,personas+1): ## Se eliminan conjuntos repetidos
			if opiniones.get(i) != None and opiniones.get(j) != None:
				if opiniones[i] == opiniones[j]:
					opiniones.pop(j)
	ans = len(opiniones)
	return ans

def main():
	inp = stdin
	cases = int(inp.readline().strip())
	line = inp.readline().strip()
	while cases > 0:
		opinions = {}
		Cpersonas,Carboles = inp.readline().strip().split()
		Cpersonas,Carboles = int(Cpersonas),int(Carboles)
		for i in range(Cpersonas): opinions[i+1] = {}
		line = [int(x) for x in inp.readline().strip().split()]
		while len(line) > 0: ## Se agregan los elementos a cada conjunto, (persona,arboles)
			opinions[line[0]][line[1]] = line[1]
			line = [int(x) for x in inp.readline().strip().split()]
		print(solve(Cpersonas,Carboles,opinions))
		if cases!= 1: print ("")
		cases -=1

main()