'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema D - Dividing Coins

Para solucionar este problema, se implemento el mismo principio que se uso durante la clase
para abordar el problema de Knap Sack, por la naturaleza del problema, no se tiene diferenciacion 
entre el objeto(la moneda) y su peso, puesto que esta vez la cantidad es el mismo peso,
debido a esto, se implemento el knapSack (Mayor ganancia en llevar una cantidad de objetos).
El parametro de peso maximo fue reemplazado por lo maximo que una persona puede tener de monedas,
que se dedujo en clase era, en el mejor de los casos, la mitad del total.
'''
from sys import stdin

def solve(value,value2,suma):
	tab,N = [ 0 for m in range(suma+1) ],len(value)
	n,m = 1,suma
	while n!=N+1:
		if m==-1:
			n,m = n+1,suma
		else:
			if value2[n-1]<=m: tab[m] = max(tab[m],value[n-1]+tab[m-value2[n-1]])
			m -= 1
	return tab[suma]


def main():
	inp = stdin
	cases = int(inp.readline().strip())
	while cases > 0:
		coins = int(inp.readline().strip())
		token = [int(x) for x in inp.readline().strip().split() ]
		value = token
		suma = sum(value)
		maxim = suma//2
		ganancia1 = solve(value,value,maxim)
		print ((suma - ganancia1) - ganancia1)
		cases -=1
main()