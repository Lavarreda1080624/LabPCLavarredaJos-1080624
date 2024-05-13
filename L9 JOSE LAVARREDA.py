print ("Ejercicio 1: operaciones aritmetricas")
#entradas
numero1 = int(input("ingrese numero entero"))
numero2 = int(input("ingrese otro numero entero"))

a = int(input("ingrese numero entero a"))
b = int(input("ingrese otro numero entero b"))
c = int(input("ingrese otro numero entero c"))
#operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
divisionEntera = numero1 // numero2
divisionModular = numero1 % numero2

#salidas
print(numero1, "//", numero2,  "=", divisionEntera )
print(numero1, "%", numero2,  "=", divisionModular )
print(numero1, "+", numero2,  "=", suma )
print(numero1, "-", numero2,  "=", resta )
print(numero1, "*", numero2,  "=", multiplicacion )

#parte2 operaciones booleanas
print ("ejercicio2: operaciones booleanas")
diferencia = numero1 != numero2
print(numero1, "!=", numero2, "=", diferencia)
diferencia2 = numero1 - numero2
print(numero1, ">=", numero2, "=", diferencia2)
diferencia3 = numero1 <= numero2
print(numero1, "<=", numero2, "=", diferencia3)
diferencia4 = numero1 == numero2
print(numero1, "==", numero2, "=", diferencia4)

#parte3 jerarquia de operaciones
print ("ejercicio3: jeraquia de operaciones")
I = a*b+c
print(I)
II = a*(b+c)
print(II)
III = a/(b+c)
print(III)
IV = (3*a)+(2*b)/ (c*c)
print(IV)