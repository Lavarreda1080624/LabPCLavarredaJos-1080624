print("Semana No.12 : ejercicio 1")
print("Menu", "a. sumatoria","b. factorial","c. Tablas de multiplicar", "d. Numero perfecto", sep="n")
#el sep da un salto de linea al imprimirse

opcion = input("Ingrese su opcion")

match opcion:
    case "a":
        n = int(input("Ingrese un numero entero positivo"))
        if(n <= 0):
            print("Error, numero debe ser mayor a cero")

        contador = 1
        sumatoria = 0
        while(contador <= n):
            sumatoria += contador
            contador += 1
            #el += va acumulando y sumando de 1 en 1 en contador es contador =contador +1

        
        print(f"Sumatoria: {sumatoria}")
    case "b":
       nf = int(input("Ingrese un numero entero"))
       if(nf <= 0):
            print("Error, numero debe ser mayor a cero")
       else:
           factorial1 = 1
           for factorial in range(1, nf+1):
               factorial1 *= factorial
               # aqui multiplica todos los numeros de 1 hasta n de 1 en 1
           print(f"El factorial de {nf} es {factorial1}")
    case "c":
        titulocol = "\t"
        for col in range(1, 11):
            titulocol+= str(col) + "\t"
        print(titulocol)

        textofila = ""
        for fila in range(1, 11):
            textofila += str(fila) + "\t"

            for col in range(1, 11):
                textofila += str(fila * col) + "\t"
            print(textofila)
            textofila = ""
