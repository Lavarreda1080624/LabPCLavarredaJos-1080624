print("Lab 15")

print("Ejercicio #1")
import math
# Para usar pi luego

print("1. Área de triángulo", "2. Área de cuadrado", "3. Área de rectángulo", "4. Área de círculo", sep ="\t\n")
areafigura = int(input("Ingrese el numero de la opción que desea realizar")) 
#No valido que no pueda haber negativo porque hay case_
match areafigura:
    case 1:
        Base = int(input("Ingrese la base del triangulo"))
        Altura = int(input("Ingrese la altura del triangulo"))
        areat = (Base * Altura)/2
        print("El area del triangulo ingresado es: ", areat)
    case 2:
        lado = int(input("Ingrese un lado del cuadrado"))
        areac = lado ** 2
        print("El area del cuadrado ingresado es: ", areac)
    case 3:
        base = int(input("Ingrese la base del rectangulo"))
        altura = int(input("Ingrese la altura del rectangulo"))
        arear = base * altura
        print("El area del rectangulo ingresado es: ", arear)
    case 4:
        radio = int(input("Ingrese el radio del circulo"))
        pi = math.pi
        areacirculo = pi*(radio**2)
        print("El area del circulo ingresado es: ", areacirculo)
    case _:
        print("Ingresar algun numero de los parametros que se le dieron")    
        

print("Ejercicio #2")
x = 0
y = 0
# def se usa par afunciones y lo de dentro dl parentesis son las entradas
def moverposicion(cambioX, cambioy):
    global x, y
    x += cambioX
    y += cambioy



opcion = 'a'
while (opcion != 'e'):
    print("El menu es:")
    print("a. sube", "b. baja", "c, izquierda", "d. derecha", "e. salir", sep ="\t\n")
    opcion = input ("Ingrese la accion que desea realizar")

    match opcion: 
        case "a":
            moverposicion(0,1)
        case "b":
            moverposicion(0,-1)
        case "c":
            moverposicion(-1,0)
        case "d":
            moverposicion(1,0)
        case _:
            print ("Error") 

print(f"La posicion del jugador es [{x}][{y}] ")