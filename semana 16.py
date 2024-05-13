import random 

print("Semana No. 16")
lista =[]

for x in range(10):
    lista.append(random.randint(0,10))

opcion ='a'
while(opcion != 'e'):
    print("Menú")
    print("a. Mostrar número","b. Promedio", "c. Longitud", "d. Posicion")
    opcion = input("Ingrese una opción: ")
    
    match opcion:
        case 'a' : #opcion mostrar numeros
            for x in range (len(lista)):
                print(f"No.{x}: {lista[x]}")

        case 'b':
            print ("PROMEDIO")
            sumatoria = 0
            for x in range (len(lista)):
                sumatoria += lista[x]
                promedio = sumatoria / len (lista)
                print (f"----- Promedio: {promedio}")
        
        case 'c':
            print("longitud de la lista")
            print (len(lista))
        
        case 'd':
            print("Pares e impares")

print("Ejercicio 2")

cantFilas = int(input("Ingrese la cantidad de filas"))
cantColumnas = int(input("Ingrese la cantidad de columnas"))

matriz = [[0 for x in range (cantColumnas)] for y in range (cantFilas)]
mayor = 0
for xFilas in range(cantFilas):
    for xCols in range (cantColumnas):
        matriz[xFilas][xCols] = random.randint(0,1000)
        
        #mayor
        if(matriz[xFilas][xCols]>mayor):
            mayor = matriz[xFilas][xCols]

print(matriz)
print(f"El numero mayor es:{mayor}")