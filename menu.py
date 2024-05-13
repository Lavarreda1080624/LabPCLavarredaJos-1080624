print("Ejercicio de menus")
print("Q25 Ranchero; 1")
print("Q50 Chapin; 2")
print("Q70 Muffin; 3")
Menu = int(input("Ingrese el numero de su menú"))
Ranchero = 25
Chapin = 50
Muffin = 70
Menusalida = int()
def switch_case():

    match Menu:
        case 1 :
            Menusalida = Ranchero
        case 2 :
            Menusalida = Chapin
        case 3 :
            Menusalida = Muffin
        case _:
            print("Quiere otro menú ")
print(f"El precio de su menú es Q{Menusalida}")

