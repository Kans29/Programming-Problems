def isPrime(n) :
    '''
    Todo Numero Entero se puede representar de la forma 6k + i
    con i = -1, 0, 1, 2, 3, o 4
    Todo primo se puede representar como 6k +- 1, excepto 2 y 3
    esto porque 2 divide a (6k + 0), (6k + 2), (6k + 4); y 3 divide a (6k + 3).

    Se valida si el numero es <= 1, si lo es, no es primo.
    Si el numero es menor o igual a 3 y mayor que 1, es primo.
    
    ''' 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True