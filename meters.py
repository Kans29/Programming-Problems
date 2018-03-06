'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema C - Potentiometers

Para dar solucion a este problema, se utilizo una estructura de datos que facilita el manejo del mismo,
Arboles de segmentos, debido a que al tener una serie de potenciometros conectados entre ellos, 
se puede manejar de una manera mas comoda la suma entre las resistencias de un rango de ellos, al igual
que la modificacion de alguno de los potenciometros.
Esta implementacion al depender de un arbol, se desarrolla en tiempo O(N) para la creacion del arbol,
y O(log(N)) para actualizaciones y busquedas en el mismo.
Esta implementacion fue tomada de las notas de clase de Analisis y Diseño de Algoritmos, periodo 2016-2
Consiste en crear un arbol de segmentos de la suma de potenciometros, y aplicar las funciones Update y Range.
'''
from sys import stdin

class segtree(object):

	def __init__(self,a):
		"""create an empty segment tree"""
		self.__a = list(a)  ## lista de los elementos del arbol a[0..N)
		self.__s = [ None for i in range(len(a)<<2) ]  ## Representacion del arbol de la suma de los rangos a[i..j) para todo i,j e 0..N
		self.__build_tree(0,0,len(a))

	def __len__(self):
		"""return the length of the collection of values"""
		return len(self.__a)  ## funcion len() de python

	def __str__(self):
		"""return the string representation of the segment tree"""
		return str(self.__s)  ## casteo a str() de una lista

	def __left(self,i):
		"""return the index of the left child of i"""
		return 1+(i<<1)  ## se maneja que el hijo izquierdo de i esta en la posicion 2i+1

	def __right(self,i):
		"""return the index of the left child of i"""
		return (1+i)<<1 ## se maneja que el hijo izquierdo de i esta en la posicion 2i+2

	def __build_tree(self,i,low,hi):
		"""store the sum of __a[low..hi) in __s[i]"""
		ans = None
		if low+1==hi:   #Si se tiene un arreglo de un unico elemento, el arbol en la posicion i toma el valor de a[low]
			ans = self.__s[i] = self.__a[low]
		else:
			## De lo contrario s[i] toma el valor de s[2i+1]+ s[2i+2], para los cuales tambien 
			## se debe construir un arbol, sucesivamente hasta llegar a la hoja, donde el largo del
			## arreglo a crear es 1
			mid = low+((hi-low)>>1)  
			ans = self.__s[i] = self.__build_tree(self.__left(i),low,mid) + self.__build_tree(self.__right(i),mid,hi)
		return ans

	def query_range(self,i,j):
		"""return the sum in the range [i..j)"""
		assert 0 <= i <= j <= len(self)
		ans = self.__query_aux(0,0,len(self),i,j)  ## Se usa una funcion auxiliar para hacer los calculos profundos
		return ans

	def __query_aux(self,i,low,hi,start,end):
		"""return the sum in the intersection of and  __a[low..hi) and __a[start..end)""" 
		ans = None
		if hi<=start or end<=low: ans = 0  ## Dado el caso de que el rango dado no se intersecte con el arreglo, se retorna 0
		elif start<=low and hi<=end: ans = self.__s[i] ## si el rango dado es mayor que el arreglo, se entrega el valor total del arreglo
		else:
			## En caso contrario, se verifica los hijos del nodo actuall de modo recursivo, retornando la suma
			## entre ellos, para que asi, si el rango a sumar se encuentra dividido, se tenga la suma al final
			mid = low+((hi-low)>>1)
			ans = self.__query_aux(self.__left(i),low,mid,start,end) + self.__query_aux(self.__right(i),mid,hi,start,end)
		return ans

	def updateValue(self,i,x):
		"""update the value of the i-th element to be x"""
		assert 0 <= i < len(self)
		self.__update_aux(0,0,len(self),i,x)  ## funcion adicional para actualizar

	def __update_aux(self,i,low,hi,j,x):
		"""uptade all the values who depend of the i-th element modified to x"""
		assert low<=j<hi
		ans = None
		if low+1==hi: ans = self.__a[j] = self.__s[i] = x  ## Si se esta en una hoja, se actualiza el valor de la hoja
		else:
			## de lo  contrario, se verifica en que seccion del arbol esta, y se actualiza recursivamente el valor
			## con los nuevos valores modificados
			mid = low+((hi-low)>>1)
			if j<mid: ans = self.__s[i] = self.__update_aux(self.__left(i),low,mid,j,x) + self.__s[self.__right(i)]
			else: ans = self.__s[i] = self.__s[self.__left(i)] + self.__update_aux(self.__right(i),mid,hi,j,x)
		return ans

def solve(potmeters,actions,cases):
	print ("Case {0}:".format(cases))
	potTree = segtree(potmeters)
	for i in actions:
		if i[0] == 'S':
			potTree.updateValue(int(i[1])-1,int(i[2]))
		else:
			ans = potTree.query_range(int(i[1])-1,int(i[2]))
			print (ans)
def main():
	inp = stdin
	N = int(inp.readline().strip())
	cases = 1
	while N != 0:
		potmeters = []
		actions = []
		for i in range(N):
			potmeters.append(int(inp.readline().strip()))
		act = inp.readline().strip()
		while act != "END":
			actions.append(act.split())
			act = inp.readline().strip()
		solve(potmeters,actions,cases)
		cases +=1
		N = int(inp.readline().strip())
		if N != 0: print("")
main()