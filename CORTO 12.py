print("Corto #12")

def perfecto(N):
    sumadefactores = 0
    for FATIMA in range(1, N):
        if N % FATIMA == 0:
            sumadefactores += FATIMA
    return sumadefactores == N

N = int(input("Ingrese un número entero positivo: "))

if N <= 0:
    print("Hola ingeniero, ingrese un numero positivo pofabo")
else:
    if perfecto(N):
        print(f"{N} es un número perfecto:)")
    else:
        print(f"{N} no es un número perfecto >:c")
