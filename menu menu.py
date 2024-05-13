print("Ejercicio de menus")
print("Q25 Ranchero; 1")
print("Q50 Chapin; 2")
print("Q70 Muffin; 3")

def switch_case(Menu):
    Ranchero = 25
    Chapin = 50
    Muffin = 70
    
    precios = {1: Ranchero, 2: Chapin, 3: Muffin}
    
    if Menu in precios:
        return precios[Menu]
    else:
        print("Opción de menú no válida")
        return 0

total = 0
while True:
    Menu = int(input("Ingrese el número de su menú (0 para terminar): "))
    if Menu == 0:
        break
    precio_menu = switch_case(Menu)
    total += precio_menu

print(f"El total de su compra es Q{total}")
