'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema A - AGTC

Para solucionar este problema, se utilizó el metodo de tabulación que se planteó en clase, en donde
se genera una matriz NM siendo N y M los tamaños de las cadenas a evaluar.
Se sabe que en la fila y la columna 0 de la matriz, el cambio va a depender del tamaño de la cadena de mayor
tamaño, asi que se inicializan de este modo.
El valor final se va a encontrar en NM, y para calcularlo, se tiene en cuentra 3 valores anteriores, el Mem[N-1][M]
que es el caso en donde se le elimina un valor a la cadena de largo N para igualar a M, el caso Mem[N][M-1] para el 
contrario, y el caso Mem[N-1][M-1] donde se evalua el caso de cambair ambos caracteres. Este prncipio se aplica para
llenar la tabla a partir de Mem[1][1]
'''
from sys import stdin

def solve(N,M,str1,str2):
	#se inicializa memoria adicional
	Mem = [ [ None for i in range(M+1) ] for j in range(N+1) ]
	Mem[0][0] = 0
	for m in range(M+1):
		Mem[0][m] = m
	for n in range(N+1):
		Mem[n][0] = n
	m,n = 1,1
	while(m != M+1):
		if(n == N+1):
			n,m = 1,m+1 # iterar matriz en 1 ciclo
		else:
			if(str1[n-1] == str2[m-1] ): #caso base, si son iguales, la cantidad de cambios no aumenta
				Mem[n][m] = Mem[n-1][m-1]
			else:  # en otro caso, se mira el minimo entre eliminar,insertar y cambiar, se suma 1 porque todos valen 1
				Mem[n][m] = 1 + min(Mem[n-1][m-1],Mem[n][m-1],Mem[n-1][m])
			n+=1
	print (Mem[N][M])

def main():
	inp = stdin
	line = inp.readline().strip().split()
	while len(line) > 0:
		x = int(line[0])
		dna1 = line[1]
		line = inp.readline().strip().split()
		y = int(line[0])
		dna2 = line[1]
		line = inp.readline().strip().split()
		solve(x,y,dna1,dna2)
main()