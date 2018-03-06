'''
UVA 12321 Gas stations

En este problema, dados un largo y una cantidad de gasolineras(cada una con su ubicacion y alcance),
se debe indicar cuantas gasolineras pueden ser eliminadas sin afectar el recorido total de la carretera.
Para este algoritmo, se implementa una solucion voraz, puesto que partiendo del inicio de la carretera,
se puede estar verificando cual es la mejor gasolinera siguiente que se encuentra en una distancia alcanzable.
Si no se encuentra ninguna, hay un area sin alcanzar, y si el total recorrino no es mayor o igual a la longitud
dada, tampoco se recorre en s totalidad. Lo que se hace es encontrar la mejor distribucion de gasolineras,
y esa cantidad se resta al total.
En vez de guardar las gasolineras como x,r siendo x ubicacion y r radio, se ubican el menor punto de alcance
y el mayor, haciendo gas = (x-r,x+r)
'''

from sys import stdin

def solve(L,G,stations):
	stations.sort()
	length,x,ans = 0,0,[]
	while x < G and length < L and stations[x][0] <= length:
		y,best = x+1,stations[x]
		while y < G and length < L and stations[y][0] <= length:
			if stations[y][1] > stations[x][1]:
				best,x = stations[y],y	
			y+=1		
		length = stations[x][1]
		ans.append(best)
		x+=1
	if length < L:
		return -1
	return G-len(ans)

def main():
	inp = stdin
	line = [int(x) for x in inp.readline().strip().split()]
	L,G,stations = line[0],line[1],[]
	while L != 0 or G != 0:
		for i in range(G):
			line = ([int(x) for x in inp.readline().strip().split()])
			stations.append([line[0]-line[1],line[0]+line[1]])
		print(solve(L,G,stations))
		line = [int(x) for x in inp.readline().strip().split()]
		L,G,stations = line[0],line[1],[]
main()