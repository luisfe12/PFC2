from random import randint

def eje11(n):
    A=[[0 for column in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = int(input("ingrresa los valores de la matriz: ..."))
    
    print(A)
    return A

def tp(matriz):
    for i in range(len(matriz)):
        for j in range(i,len(matriz)):
            axu = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = axu
            #print(matriz)
    print(matriz)
    return matriz


n = int(input("ingresa el tamaño de la matriz nxn: ...."))

Matriz_A = eje11(n)
Matriz_t = tp(Matriz_A)

for i in range(len(Matriz_t)):
    print(Matriz_t[i])