'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema B - The Stern-Brocot Number System

Para solucionar este algoritmo, se partio del principio de busqueda binaria dada la naturaleza del problema.
En este problema, se nos da un arbol Stern-Brocot, para el cual cada uno de sus nodos escrito de la forma
m/n, esta dado por la suma de un m1+m2/n1+n2 anteriores. Cada m,n es una pareja de primos relativos.
Se tienen 2 casos bases, o por decirlo de una forma, elementos iniciales, los cuales son m1 = 0 y n1 = 1, junto con
m2 = 1 y n2 = 0, por lo que se sabe que hay un m3/n3, que viene siendo 1/1 por lo dicho anteriormente.
Partiendo del hecho de que se reciben siempre fracciones positivas, se puede hacer busqueda binaria teniendo
como punto de partida, escoger si buscar en la seccion 0 < n < 1 o en la seccion 1 < n < k, para algun k
que es mayor que el n.
Despues de saber esto, se sabe que en algun momento teniendo m1,m2,n1,n2, se va a llegar a un m3,n3 que sea igual
a M,N de la entrada, y que los limites se acomodan dependiendo del lado en el que se encuentr la fraccion que ingresa.
Las condiciones se pueden revisar viendo al denominador de la fraccion frente al numerador, ambos incrementados
en los valores que se tienen actualmente, partiendo del hecho de que a/b * b/a = 1, se puede comenzar a buscar,
dado el caso de que el denominador sea mayor, indica que la fraccion se encuentra a la izquierda, en caso contrario, a 
la derecha.
'''

from sys import stdin
def solve(M,N):
	m1,n1 = 0,1
	m2,n2 = 1,0 
	m3,n3 = m1+m2,n1+n2
	bandera = False
	respuesta = ""
	while bandera == False:
		if m3 == M  and n3 == N: ## encuentra los M y N que ingresan
			bandera = True
		elif (m3 * N > n3 * M) and bandera == False: ## indica que el valor M,N esta a la izquierda de m3,n3
			respuesta+='L'
			n1 = m3 
			n2 = n3
		elif (m3 * N < n3 * M) and bandera == False: ## indica que el valor M,N esta a la derecha de m3,n3
			respuesta+='R'
			m1 = m3
			m2 = n3
		m3 = m1 + n1
		n3 = m2 + n2
	print(respuesta)

def main():
	inp = stdin
	line = [int(x) for x in inp.readline().strip().split()]
	while (line[0]*line[1] != 1) :
		solve(line[0],line[1])
		line = [int(x) for x in  inp.readline().strip().split()]
		

main()