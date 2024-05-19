print("Corto #4")

X = [[0, 0, 0, 0, 0, 0, 0, 0],    #matrices para guardar los resultados
    [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]
for i in range(len(X)):  # recorremos filas
    for j in range(len(X[0])):  # recorremos columnas
        # Verificamos si la suma de los índices es impar
        if (i + j) % 2 != 0:
            X[i][j] = 1

# Imprimimos la matriz para verificar
for fila in X:
    print(fila)

