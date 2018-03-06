"""
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema A - Where is the Marble?

Para dar solucion al problema, se implementa el principio de busqueda binaria, partiendo del hecho de que se
tiene el arreglo de canicas ordenado, se puede tomar un punto medio del arreglo para revisar si la canica
x que se esta buscando es mas grande o mas pequeña que la mitad, para asi descartar algun lado. Este proceso
se realiza hasta que se encuentra alguna vez en la que se cumpla marble[mid] == x, en donde lo que se hace es
comenzar a mirar las canicas anteriores para encontrar la primera ocurrencia de esta. En el peor de los casos
el ciclo se termina y retorna inicio, que puede ser la canica o simplemente que no la encontró.
"""

from sys import stdin

marble,lenm = None,None

def solve(x):
  global marble,lenm
  inicio = 0
  fin = lenm 
  while(inicio+1 != fin):
    mid = inicio + ((fin-inicio)//2)
    if(marble[mid] == x):
      while(marble[mid] == x):
        mid = mid -1
      return mid+1
    elif(marble[mid] < x):
      inicio = mid
    else:
      fin = mid
  return inicio

def main():
  global marble,lenm
  inp = stdin
  cas = 1
  lenm,lenq = [ int(x) for x in inp.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(inp.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(cas))
    for q in range(lenq):
      x = int(inp.readline())
      ans = solve(x)
      if ans==-1 or marble[ans]!=x:
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    cas += 1

main()
