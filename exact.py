"""
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema C - Exact Sum

Para dar solucion al problema, inicialmente, para facilidad de la busqueda, se realiza un .sort() al
arreglo de entrada, con lo que sabemos que en lo posible, la mejor solucion, es decir, los 2 libros
que se va a retornar, lo mas posiblemente sean 2 numeros relativamente cercanos(iguales en el mejor
de los casos) y se encuentran en la "mitad" del arreglo.
Con este principio, se parte ubicando 2 apuntadores, un apuntador al inicio del arreglo, posicion 0, 
y otro en el ultimo elemento.
El proceso de busqueda e realiza siempre que el apuntador inferior sea estrictamente menor que el mayor
(low < high) y lo que se hace es comparar si la suma entre estos 2 apuntadores es igual a el dinero 
que se tiene. Si es igual, se guardan los valores en variables de reserva y se actualizan los apuntadores
el menor aumentando y el mayor disminuyendo. 
Dado el caso de que la suma sea mayor que el dinero, lo que se hace es restar el acumulador mayor, para asi 
tratar de hacer cumplir la igualdad, y en caso contratio, cuando es menor, se incrementa el apuntador menor.
"""

from sys import stdin

price = None

def solve(n,m):
  global price
  price.sort()
  low = 0
  high = len(price)-1
  while(low < high):
    if(price[low] + price[high] == m):
      l1 = price[low]
      l2 = price[high]
      low = low + 1
      high = high - 1
    elif(price[low] + price[high] > m):
      high = high - 1
    else:
      low = low + 1
  return l1,l2

def main():
  global price
  inp = stdin
  line = inp.readline().strip()
  while len(line)>0:
    n = int(line)
    price = [ int(x) for x in inp.readline().strip().split() ]
    m = int(inp.readline().strip())
    ans = solve(n,m)
    print('Peter should buy books whose prices are {0} and {1}.\n'.format(ans[0],ans[1]))
    inp.readline()
    line = inp.readline().strip()

main()
