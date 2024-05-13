print( "Operaciones entre matrices")
X = [[5, 19, 6],    #Definimos matriz X
     [8, 15, 4],
     [10, 7, 8]]

Y = [[28, 8, 12], #Definimos matriz Y
     [18, 7, 3],
     [1, 5, 4]]
print (X)
print(Y)
resultados = [[0, 0, 0],    #matrices para guardar los resultados
    [0, 0, 0],
     [0, 0, 0]]
#suma de matrices
for i in range (len(X)): #recorremos filas
    for j in range (len(X[0])): #recorremos columnas
        resultados [i][j] = X[i][j] + Y[i][j] #guardamos resultados
print ("La suma es:")
for res in resultados:
    print (res)
#resta
for f in range (len(X)): #recorremos filas
    for c in range (len(X[0])): #recorremos columnas
        resultados [f][c] = X[f][c] - Y[f][c] #guardamos resultados
print ("La resta es:")
for resta in resultados:
    print (resta)
#multiplicación
for L in range (len(X)): #recorremos filas
    for J in range (len(X[0])): #recorremos columnas
        resultados [L][J] = X[L][J] * Y[L][J] #guardamos resultados
print ("La multiplicacion es:")


print("Ejercicio de pares")
for multiplicacion in resultados:
    print (multiplicacion)

print("Elementos pares de la primera matriz (X):")
for i in range(len(X)):  # recorremos filas
    for j in range(len(X[0])):  # recorremos columnas
        if X[i][j] % 2 == 0:  # verificamos si el elemento es par
            print(X[i][j])

print("Elementos impares de la segunda matriz (Y):")
for i in range(len(Y)):  # recorremos filas
    for j in range(len(Y[0])):  # recorremos columnas
        if Y[i][j] % 2 != 0:  # verificamos si el elemento es impar
            print(Y[i][j])