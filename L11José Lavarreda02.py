print("Semana No11 : ejercicio 1")
n = int(input("Ingrese un numero mayor a cero"))

if (n <= 0):
    print("error, debe de ser mayor a cero")
#Definicion de variables para fibonacci
a = 0
b = 1
c = 0

i = 2
resultado = " "
#str convertir numero a texto (string)
if(n > 0):
    resultado = str(a)

    if(n > 1):
        resultado = resultado + " ," + str(b)
    #ciclo
    while (i < n):
        c= a + b
        resultado = resultado + " ," + str(c)
        a = b
        b = c
        i = i + 1
    print(resultado)
else:
    print(resultado)

n2 = int(input("Ingrese un numero mayor a cero"))

if (n2 <= 0):
    print("Error, debe ser mayor a 0")
#ejercicio A
calculoA = 0
for xA in range( 1, n2 + 1):
    calculoA += 1/xA
print("El resultado de A es: " , calculoA)

