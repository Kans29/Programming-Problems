from sys import stdin

class dforest(object):

	def __init__(self,size):
		self.parent = [i for i in range(size)]
		self.rank = [1 for i in range(size)]
		self.depth = [0 for i in range(size)]


	def find(self,x):
		root = self.parent[x]
		ans = root
		if root != self.parent[root]:
			y = self.parent[root]
			self.parent[x] = self.find(y)
			self.depth[x] += self.depth[y]
		return root

	def union(self,x,y):
		rx,ry = self.find(x),self.find(y)
		d = self.find(y)
		if self.rank[rx] > self.rank[ry]:
			self.parent[ry] = rx
			self.depth[rx] += d + 1
			self.depth[ry] -= self.depth[rx]
		else:
			self.parent[rx] = ry
			self.depth[rx] += d + 1 - self.depth[ry]
			if self.rank[rx] == self.rank[ry]:
				self.rank[rx] +=1

	def size(self,x):
		ans = self.depth[x]
		return ans

def kruskal(graph,cf):
	graph.sort( key = lambda x : x[2]) 
	df,n,ans = dforest(cf-1),0,0
	while n != len(graph):
		if(df.find(graph[n][0]) != df.find(graph[n][1])):
			ans += graph[n][2]
			df.union(graph[n][0],graph[n][1])
		n+=1
	print(ans)

def main():
	inp = stdin
	cases = int(inp.readline().strip())
	while cases > 0:
		line = inp.readline().strip()
		lenf = int(inp.readline().strip())
		freckles = []
		for i in range(lenf):
			line = [float(x) for x in inp.readline().strip().split()]
			freckles.append((line[0],line[1]))
		graph = []
		for i in range(len(freckles)):
			for j in range(i+1,len(freckles)):
				graph.append((i,j,((((freckles[i][0]-freckles[j][0])**2)+((freckles[i][1]-freckles[j][1])**2))**(1/2))))
		kruskal(graph,lenf)
		cases -=1
main()