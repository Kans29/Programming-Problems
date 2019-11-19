"""
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema D - Train Swapping

Para esta solucion se usa el principio de ordenamiento con conteo de intercambios adyacentes.
Debido al limite de tiempo, se reconoce que se debe usar un algoritmo con una complejidad menor
que algoritmos como insertionSort o bubble, tales como pueden ser un QuickSort o un MergeSort, 
que poseen complejidad de O(n log(n)).

El algoritmo fue tomado de https://goo.gl/1HTDlc, y fue pensado en colaboracion con Mateo Valencia.
"""
from sys import stdin

MAX = 25010
train = [ None for i in range(MAX) ]
memo = [ None for i in range(MAX) ]


def merge(izq, der):
    result = []
    i, j, count = 0, 0, 0
    while (i < len(izq) and j < len(der)):
        if (izq[i] <= der[j]):
            count = count + j
            result.append(izq[i])
            i = i + 1
        else:
            result.append(der[j])
            j = j + 1
    count = count + j*(len(izq)-i) #Factor de multiplicacion de cantidad de cambios durante la mezcla del merge
    result = result + izq[i:]
    result = result + der[j:]
    return count, result

def mergeSort(list):
    if (len(list) <= 1):
        return 0, list
    mid = len(list)//2
    a, izq = mergeSort(list[:mid])
    b, der = mergeSort(list[mid:])
    c, ans = merge(izq, der)
    tot = a + b + c
    return tot, ans
    
def solve(n):
  global train,memo,count
  count = mergeSort(train[:n])
  return count[0]

def main():
  global train
  inp = stdin
  cases = int(inp.readline().strip())
  while cases>0:
    n = int(inp.readline().strip())
    tok = inp.readline().strip().split()
    for i in range(n): train[i] = int(tok[i])
    print('Optimal train swapping takes {0} swaps.'.format(solve(n)))
    cases -= 1

main()
