A2 = [[1,4,5,12],[-5,8,9,0]]

#print ("A =", A)
print("A[0] =", A2[0])
print("A[1] =", A2[1])
#ej 2
for fila in A2:
    print(A2)

#Ejemplo #3
for filaej in A2:
    for elemento in filaej:
        print(elemento)
#Ejemplo #4
for row in A2:
    for element in row:
        print(element, end ='') #end agrega al final algo en este caso un salto de linea
    print () #Imprime un una fila en blanco 

#Operaciones entre matrices
print( "Operaciones entre matrices")
X = [[12, 7, 3],    #Definimos matriz X
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1], #Definimos matriz Y
     [6, 7, 3],
     [4, 5, 2]]

resultados = [[0, 0, 0],    #matrices para guardar los resultados
    [0, 0, 0],
     [0, 0, 0]]

for i in range (len(X)): #recorremos filas
    for j in range (len(X[0])): #recorremos columnas
        resultados [i][j] = X[i][j] + Y[i][j] #guardamos resultados

for res in resultados:
    print (res)