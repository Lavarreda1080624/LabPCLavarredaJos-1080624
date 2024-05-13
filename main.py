import operaciones

a = int(input("Ingrese un número "))
b = int(input("Ingrese un número menor al anterior"))
if b > a:
    print("error: te dije que pusieras un numero menor que el anterior ")
    b = int(input("Ingrese un número menor al anterior"))

print(operaciones.suma(a,b))
print(operaciones.resta(a,b))
print(operaciones.multiplicacion(a))


# array de nombres 
import arreglos

from arreglos import alreves, cantidadletras

nombre = input("Escriba su nombre: ")

nombre_al_reves_resultado = alreves(nombre)
cantidad_letras_resultado = cantidadletras(nombre)

print("Su nombre al revés es:", nombre_al_reves_resultado)
print("Su nombre tiene", cantidad_letras_resultado, "letras")