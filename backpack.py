"""
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema B - Winterim Backpacking Trip

Para dar solucion al problema, se implemento la idea que se nos planteó durante la clase,
en la que se maneja un principio de busqueda binaria, en donde se tiene como punto minimo
el valor 0 y como punto maximo el recorrido mas largo posible, es decir, la suma de todos
los elementos de la lista sites. Teniendo esto, se saca el punto medio entre estos y
tal punto medio se asume como el recorrido maximo que voy a considerar para evaluar.
Se maneja un contador que va aumentando cada vez que avanza un sitio, y cada vez que
el contador supera al maximo recorrido por dia, se incrementa el contador noches, indicando
que en ese punto se descansa y se reinicia el contador acumulador, asi hasta el final.
Habiendo recorrido todos los sitios, se evalua si la cantidad de noches cumple con lo
solicitado en la entrada( noche <= k) y el valor es mayor o igual que el trayecto
mas grande entre 2 campamentos, significa que se puede descansar mas noches, y se actualiza
el high, el low se actualiza en caso contrario.
"""

from sys import stdin

MAX = 610
sites = [ None for i in range(MAX) ]
sums,omin,omax,n,k = None,None,None,None,None

def solve():
  global sites,sums,omin,omax,n,k
  high = sums
  low = 0
  while(low+1 != high):
    mid = low + ((high-low)//2)
    noche = 0
    acumulado = 0
    j = 0
    while( j < n):
      if( acumulado + sites[j] > mid):
        noche = noche + 1
        acumulado = sites[j]
      else:
        acumulado = acumulado + sites[j]
      j = j+1
    if(noche <= k and mid >= omax):
      high = mid
    else:
      low = mid
  return high

def main():
  global sites,sums,omin,omax,n,k
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    n,k = [ int(x) for x in l.split() ]
    n += 1
    omin,omax,sums = float('inf'),float('-inf'),0
    for i in range(n):
      sites[i] = int(inp.readline().strip())
      if sites[i]>omax: omax = sites[i]
      if sites[i]<omin: omin = sites[i]
      sums += sites[i]
    if sums==0:
      print(0)
    else:
      print(solve())
    l = stdin.readline().strip()

main()
