'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema A - Abnormal 89's

Para dar solucion a este problema, se utilizo el algoritmo de busqueda de subcadenas Knuth-Morris-Pratt
(KMP), el cual verifica si una cadena B existe en una A usando automatas de fallo.
Para esta solucion, se debe encontrar 3 casos, si la palabra A es Palindrome (Se lee igual de izquierda
a derecha y de derecha a izquierda), Alindrome (La union de 2 palindromes) o ninguna de las 2.
Para verificar si una palabra es palindrome, se puede verificar si el inverso es una subcadena del mismo
es decir, llamar a KMP(A,A') = True. Esto no es suficiente para alindrome, por lo que se extiende la solucion.
Asi como A' existe en A, A' debe existir en A+A, terminando la comparacion en la mitad, o en el final.
Con esto, se sabe que KMP maneja 2 iteradores, i para la cadena A+A y j para la cadena A', si durante el
KMP j alcanza el len(A'), es que A' e A+A, al encontrarlo, si i(posicion en A+A)- j = 0 o = len(A'), la palabra
es palindrome, si j nunca alcanza len(A'), la palabra es simple, y en el caso en que i - j sea diferente de 0
o de len(A') indica que se encontro A' en una seccion de A+A distinta a [0..(len(A)) y [len(A)..2len(A)), por lo
que es alindrome.
'''
from sys import stdin

def arrayBuild(P):
	N = len(P)
	A = [0 for x in range(N)]
	i,j = 1,0,
	while i < N:
		if P[i] == P[j]:
			j=j+1
			A[i] = j
			i+=1
		else:
			if P[i] != P[j] and j != 0:
				j = A[j-1]
			else:
				A[i] = j
				i+=1
	return A
def patternSearch(A,B):
	M = len(A)
	N = len(B)
	array = arrayBuild(B)
	i,j,ans,bandera = 0,0,-1,True
	while i < M:
		if A[i] == B[j]:
			i,j=i+1,j+1
		else:
			if A[i] != B[j] and j != 0:
				j = array[j-1]
			else:
				i +=1
		if j == N:
			ans = i-N 
			if ans > 0 and ans < N:
				bandera = False
			j = array[j-1]
	if bandera == False:
		ans= -10
	return ans
def solve(A):
	B = A[::-1]
	A = A+A
	ans = patternSearch(A,B)
	#print (ans)
	if  ans == 0 or ans == len(B):
		print ("palindrome")
	elif ans == -1:
		print ("simple")
	else:
		print ("alindrome")
def main():
	inp = stdin
	line = inp.readline().strip()
	cases = int(line)
	while cases > 0:
		line = inp.readline().strip()
		solve(line)
		cases -=1
main()