"""
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema D - Partitioning by Palindrome

Para dar solucion a este problema, se partió del principio de programacion dinamica implementado en
clase con este problema. En el cual, tomamos un n en el arreglo de largo N, en este caso denominado A. 
Teniendo esta referencia, se escoge un k, tal queel k recorre todos los elementos tales que 0<= k < n 
revisando la cantidad de subpalindromes posibles.
Partimos del hecho de que toda cadena de largo 1 es palindrome, por lo que en el mejor de los casos, 
se recorren todos los k posibles entre todos los n del arreglo, haciendo que la cantidad minima de 
subpalindromes sea la cantidad de elementos, o que la cantidad minima sea 1, es decir, una palindrome.
Cada vez que se confirma un subpalindrome desde k hasta n, se actualiza el valor de minima cantidad de
subpalindromes, para asi, tener al final el minimo.
"""
from sys import stdin
## Se define una funcion pal, que recibe como parametro un arreglo, y 2 posiciones entre las cuales 
## se desea saber si la palabra que encierran es o no palindrome
def palindrome(k,n,A):
	i = k
	j = n-1
	while i < j:
		if A[i] != A[j]:
			return False
		i,j = i+1,j-1
	return True
## Se plantea una solucion por tabulacion, que se toma un tiempo de ejecucion O(n^3) y ocupa espacio
## O(n)
def solve(A):
	N = len(A)
	## se inicializa en infinito, dado que se busca usar min, y todos los valores a tratar son menores que el mismo
	tab,n = [ float('inf') for i in range(N+1) ],1  
	tab[0] = 0  ## se tiene claro que al iniciar no hay palindromes, porque n=k=0, por lo que se puede asumir.
	while n!= N+1:
		for k in range(n):
			if palindrome(k,n,A):
				tab[n] = min(tab[n],1+tab[k])
		n += 1
	return tab[N] 

def main():
	inp = stdin
	cases = int(inp.readline().strip())
	while cases > 0:
		string = inp.readline().strip()
		print(solve(string))
		cases = cases-1
main()