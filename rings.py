'''
Problema UVA 10301 Rings and Glue

Dados n circulos, con sus centros (x,y) y su radio R, encuentre el mayor grupo de circulos intersectados
en un punto, por resumirlo de una forma.
La solucion parte del concepto de conjuntos disjuntos, en el cual, inicialmente cada circulo es un conjuntos
disjunto de los demas, y se verifica la interseccion de uno a uno, si se da la interseccion, entonces, se
realiza la union de los arboles que representan cada circulo.
Dicha union se puede calcular a traves de una desigualdad triangular, donde si la distancia de los centros de 
los circulos es menor que la suma de sus radios y mayor que la resta, estan intersectados, en cualquier
otro caso, o uno esta contenido dentro de otro, o estan apartados y no se intersectan.
Al final, se retorna el mayor tamaño de la lista de arboles disjuntos.
'''
from sys import stdin

class dforest(object):

	def __init__(self,size=100):
		self.__parent = [ i for i in range(size) ]
		self.__size = [ 1 for i in range(size) ]
		self.__rank = [ 0 for i in range(size) ]

	def __len__(self):
		return len(self.__parent)

	def __contains__(self,x):
		return 0 <= x < len(self)

	def find(self,x):
		assert x in self
		if self.__parent[x]!=x:
			self.__parent[x] = self.find(self.__parent[x])
		return self.__parent[x]

	def union(self,x,y):
		assert x in self and y in self
		rx,ry = self.find(x),self.find(y)
		if rx!=ry:
			nx,ny = self.__rank[rx],self.__rank[ry]
			if nx<=ny:
				self.__parent[rx] = ry
				self.__size[ry] += self.__size[rx]
				if nx==ny: self.__rank[ry]+=1
			else:
				self.__parent[ry] = rx
				self.__size[rx] += self.__size[ry]

	def size(self,x):
		assert x in self
		return self.__size[self.find(x)]


def solve(n,rings):
	df,i,maxim = dforest(n),0,0
	while i < n:
		ra,j = rings[i],i+1
		while j < n:
			rb = rings[j]
			d = ((ra[1]-rb[1])**2 + (ra[0]-rb[0])**2)**(1/2)
			if abs(ra[2]-rb[2]) <= d <= abs(ra[2]+rb[2]):
				df.union(i,j)
			j+=1
		i+=1
	for i in range(df.__len__()):
		var = df.size(i)
		if var > maxim:
			maxim = var
	return maxim

def main():
	inp = stdin
	n = int(inp.readline().strip())
	rings = []
	while n != -1:
		N = n
		while N > 0:
			r = [float(x) for x in inp.readline().strip().split()]
			N -=1
			rings.append(r)
		ans = solve(n,rings)
		if ans == 1:
			print("The largest component contains {0} ring.".format(ans))
		else:
			print("The largest component contains {0} rings.".format(ans))
		n = int(inp.readline().strip())
		rings = []
main()