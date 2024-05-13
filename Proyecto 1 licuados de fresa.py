# licuados de fresa a 20.0Q
print("Buen dia cual es su nombre :)")
nombre = input()
print ("mucho gusto", nombre)
input("Ingrese su NIT: ")

#Precio base del licuado 
licuadopordefecto = 20
print("este es el precio de nuestro licuado base Q", licuadopordefecto)
     #cambios al pedido

#Azucar
cucharadasdeazucar = int(input("cuantas cucharadas de azucar quiere" ))

match cucharadasdeazucar:
    case 1:
        cucharadasdeazucarf = print("El precio es Q",licuadopordefecto+0.5)
    case 2:
        cucharadasdeazucarf = print("El precio es Q", licuadopordefecto+1)
    case _:
        print("No se puede agregar mas de 2 cucharadas cuida tu salud:)")

#modificar leche 

print("Selecciona un numero dependiendo de que leche quieras ;)")
print("1. Sin leche (únicamente con agua)")
print("2. Leche deslactosada")
print("3. Leche entera.")
print("4. Leche de soya")
tipodeleche = int(input("Ingrese el numero de la opcion de leche que quiere"))
licuadocontipodeleche = ""
match tipodeleche:
    case 1:
        licuadocontipodeleche = print("El precio es Q", cucharadasdeazucarf-2)
    case 2:
        licuadocontipodeleche = print("El precio es Q", cucharadasdeazucarf+0)
    case 3:
        licuadocontipodeleche = print("El precio es Q", cucharadasdeazucarf+0)
    case 4:
        licuadocontipodeleche = print("El precio es Q", cucharadasdeazucarf+3)
    case _:
        print("Elegir un numero de los que dije >:c")

#agrandar producto
print("¿Desea agrandar el licuado?")
print("1. Sí")
print("2. No")

Agrandar = input("Ponga el numero de lo que quiere realizar")
agrandarf = ""
match Agrandar:
    case 1:
        agrandarf = print("El precio es Q", licuadocontipodeleche*1.05)
    case 2:
        agrandarf = print("El precio es Q", licuadocontipodeleche*1)
    case _:
        print("!Solo se puede elegir numeros del 1 al 2 >:c!")

#Confirmar pedido

