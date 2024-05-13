print ("semana No.10  ejercicios 1")
mesEntrada = int(input("Ingrese un numero del 1 al 12"))
mesSalida = ""
match mesEntrada:
    case 1 :
        mesSalida = "Enero"
    case 2 :
        mesSalida = "Febrero"
    case 3 :
        mesSalida = "Marzo"
    case 4 :
        mesSalida = "Abril"
    case 5 :
        mesSalida = "Mayo"
    case 6 :
        mesSalida = "Junio"
    case 7 :
        mesSalida = "Julio"
    case 8 :
        mesSalida = "Agosto"
    case 9 :
        mesSalida = "Septiembre"
    case 10 :
        mesSalida = "Octubre"
    case 11 :
        mesSalida = "Noviembre"
    case 12 :
        mesSalida = "Diciembre"
    case _:
        print("Error: El numero a ingresar debe estar contenido entre 12 ")
print(f"MES: {mesSalida}")

#ejercicio 2

print("Semana 10 ejercicio 2")
a = int(input ("ingrese un primer numero mayor a 0"))
b = int(input ("ingrese un primer numero mayor a 0"))
c = int(input ("ingrese un primer numero mayor a 0"))

if(a <= 0 or b <=0 or c <=0 ):
    print("Error, el numero debe de ser mayor a cero")

if(a>b):
    if(a>c):
        print("El numero A es mayor que B y que C") 
    else:
        if(a == c):
            print("A es mayor a B y A es igual a C")
        else: 
            print("A es mayor a B y A es diferente a C")
else:
    if(a == b):
        if(a > c):
            print("A es igual a B y A es mayor que C")
        else:
            if(a == c):
                print("A es igual a B y A es igual a C")
            else:
                print("A es igual a B y A no es igual a C")
    else: 
        if(b>c):
            print("A es menor que B y B es mayor que C")        
        else: 
            if(b==c):
                print("A es menor que B y B es igual que C")
            else: 
                print("A es menor que B y B es menor que C")
                
#ejercicio 3 
print("Semana No. 10: ejercicio 3 signos zodiacales JCLP1080624")

dia = int(input("Ingrese el día de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))

if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Piscis"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "Capricornio"
else:
    signo = "Fecha inválida"

print("Tu signo zodiacal es:", signo)