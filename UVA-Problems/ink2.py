'''
Pontificia Universidad Javeriana Cali
Final project of 'Analisis y Diseño de Algoritmos' - 2017-1
Student: Daniel Cano Salgado
Code: 1872525
Commitment sentence:
	"Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
	 a seguir los más altos estándares de integridad académica."
UVA Problem - 11665  Chinese Ink
'''
from sys import stdin
INF = 10**5 
class dforest(object):

	def __init__(self,size=100):
		"""Creates a empty disjoint forest"""
		self.__parent = [ i for i in range(size) ]
		self.__size = [ 1 for i in range(size) ]
		self.__rank = [ 0 for i in range(size) ]

	def __len__(self):
		"""Return the number of elements of the forest"""
		return len(self.__parent)

	def __contains__(self,x):
		"""Tells if an element x is in the forest"""
		return 0 <= x < len(self)

	def find(self,x):
		"""Returns the class index of the tree where x belongs"""
		assert x in self
		if self.__parent[x]!=x:
			self.__parent[x] = self.find(self.__parent[x])
		return self.__parent[x]

	def union(self,x,y):
		"""Makes the union between 2 trees"""
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
		"""Returns the size of a tree"""
		assert x in self
		return self.__size[self.find(x)]

class vertex(object):

	def __init__(self,x,y):
		"""Creates a dot in 2D with coordinates (x,y)"""
		self.x = x
		self.y = y

def pointInSegment(p,q,r):
	"""Tells if a point r is in |p,q|"""
	if (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y)):
		return True
	return False

def orientation(p,q,r):
	"""Given 3 points, tells if they are oriented clockwise, counter-clockwise or if they are collinear"""
	val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
	if val == 0: return 0
	return 1 if val > 0 else 2

def segmentIntersect(a1,a2,b1,b2):
	"""Tells if segment |a1,a2| intersects with |b1,b2|"""
	o1 = orientation(a1, a2, b1)
	o2 = orientation(a1, a2, b2)
	o3 = orientation(b1, b2, a1)
	o4 = orientation(b1, b2, a2)

	if o1 != o2 and o3 != o4:return True
	if o1 == 0 and pointInSegment(a1, b1, a2):return True
	if o2 == 0 and pointInSegment(a1, b2, a2):return True
	if o3 == 0 and pointInSegment(b1, a1, b2):return True
	if o4 == 0 and pointInSegment(b1, a2, b2):return True
	return False

def polygonContention(polygon,x):
	"""Tells if a point x is inside a polygon"""
	count,verInf = 0,vertex(x.x,INF)
	for i in range(0,len(polygon)-1):
		if segmentIntersect(polygon[i],polygon[i+1],x,verInf) and count<2: count+=1
	return True if count == 1 else False

def solve(N,polygons):
	ans,p1,df = 0,0,dforest(N)
	while p1 != N-1:
		p2 = p1+1
		while p2 != N:
			root1,root2 = df.find(p1),df.find(p2)
			if root1 != root2:
				intersection,contain,i = False,False,0
				while i <= len(polygons[p1])-2 and intersection == False:
					j = 0
					while j <= len(polygons[p2])-2 and intersection == False:
						intersection = segmentIntersect(polygons[p1][i],polygons[p1][i+1],polygons[p2][j],polygons[p2][j+1])
						j+=1
					i+=1
				if intersection == False:
					contain = polygonContention(polygons[p1],polygons[p2][0]) or polygonContention(polygons[p2],polygons[p1][0])
				if intersection or contain:
					df.union(p1,p2)
					ans+=1
			p2+=1
		p1+=1
	return N-ans

def main():
	inp = stdin
	N,ans = int(inp.readline().strip()),[]
	while N != 0:
		polygons,n = [],N
		while n > 0:
			line = inp.readline().strip().split()
			p = [vertex(int(line[x]),int(line[x+1])) for x in range(0,len(line)-1,2)]
			p.append(p[0])
			polygons.append(p)
			n-=1
		ans.append(str(solve(N,polygons)))
		N = int(inp.readline().strip())
	print('\n'.join(ans))
main()