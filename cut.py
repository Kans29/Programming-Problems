'''
Daniel Cano Salgado - Analisis y diseño de algoritmos
Solucion al problema C - Cutting Sticks

Para solucionar este problema, se implemento el metodo de memorización, a través del cual, se creo
una tabla de 51,51, asumiendo el peor de los casos, y en ella se iban guardando datos ya previamente
calculados. En esta implementacion toca limpiar la memoria adicional despues de cada caso.
Lo que se hace es, para el largo de la cadena, se verifican todos los casos posibles de cortes
y se escoge el mejor de ellos, guardandolo en Mem.
Se hace comparaciones de el minimo entre cuts[0..k] y cuts[k..n] escogiendo el mejor en cada ocacion.
'''

from sys import stdin
MAX = 51
Mem = [[ float('inf') for i in range (MAX)] for j in range (MAX)]
CutPlaces = [ None for i in range(MAX)]

def solve(inicioStick, finStick, i, j):
    global Mem, CutPlaces
    
    largo = finStick - inicioStick
    if (i == j): ## Indica que se debe tomar todo el largo del palo porque no hay elementos en la lista de cortes
        return largo 
    elif (i > j): ## los indices estarian cambiados, indicando que no hay para revisar en la lista de cortes
        return 0 
    elif (Mem[i][j] != float('inf')): ## el valor de los minimos cortes entre i y j ya fue calculado, se evita recalcular
        return Mem[i][j] 
    k = i ## se ubica el iterador en la posicion inicial que se tiene de CutPlaces
    while (k <= j): ## El caso de i,j no ha sido calculado, entonces se calcula
        ## se escoge el minimo entre el valor que se tiene en la Memla, o entre el valor calculado,
        ## valor que se obtiene verificando desde el inicio del palo, hasta la posicion donde se ubique
        ## el indice izquierdo en cutPlaces[], el cual empieza en cero, mas lo que hay desde cutPlaces en i
        ## hasta el final, y a todo esto se le suma el valor de toda la barilla.
        Mem[i][j] = min(Mem[i][j], solve(inicioStick, CutPlaces[k], i, k - 1) + solve(CutPlaces[k], finStick, k + 1, j) + largo) 
        k += 1
    return Mem[i][j] 

def main():
    global CutPlaces, Mem
    
    inp = stdin
    StickLength = int(inp.readline())
    while (StickLength != 0):
        TotalCuts = int(inp.readline()) 
        CutPlaces = [int (x) for x in inp.readline().strip().split()] 
        for i in range(0,MAX):
            for j in range(0,MAX):
                Mem[i][j] = float('inf')  ## se borran los datos que se tenian en Mem
        ans = solve(0, StickLength, 0, TotalCuts - 1)
        print('The minimum cutting is {0}.'.format(ans))
        StickLength = int(inp.readline())
main()
