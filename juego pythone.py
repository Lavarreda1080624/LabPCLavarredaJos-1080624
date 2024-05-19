import random

# Introducción del juego
def intro():
    print("Bienvenido a Code Warriors: Python Edition")
    print("Eres un guerrero cibernético en una misión para derrotar a una IA malvada.")
    print("Usa tus habilidades de programación en Python para superar los desafíos.")
    print("¡Buena suerte!\n")

# Primer nivel: Variables y Operaciones
def level_1():
    print("Nivel 1: Variables y Operaciones Básicas")
    print("Tu primer desafío es calcular el poder de tu arma.\n")
    
    power_base = 50
    power_bonus = 20

    print(f"Tu poder base es {power_base}.")
    print(f"Tu bono de poder es {power_bonus}.")
    power_total = power_base + power_bonus
    print(f"Tu poder total es {power_total}.\n")
    
    print("¡Has completado el Nivel 1!\n")
    return True

# Segundo nivel: Condicionales
def level_2():
    print("Nivel 2: Condicionales")
    print("Te enfrentas a un enemigo. Debes decidir si atacar o defenderte.\n")
    
    enemy_power = random.randint(30, 70)
    player_power = 60

    print(f"El poder del enemigo es {enemy_power}.")
    
    if player_power > enemy_power:
        print("Tu poder es mayor. ¡Atacas al enemigo y ganas!")
    else:
        print("El poder del enemigo es mayor. Te defiendes y esperas una mejor oportunidad.")
    
    print("\n¡Has completado el Nivel 2!\n")
    return True

# Tercer nivel: Bucles
def level_3():
    print("Nivel 3: Bucles")
    print("Debes hackear un sistema de seguridad. Necesitas probar varias combinaciones.\n")
    
    password = "python"
    attempts = 5

    for attempt in range(1, attempts + 1):
        guess = input(f"Intento {attempt} de {attempts}. Ingresa la contraseña: ")
        if guess == password:
            print("Contraseña correcta. ¡Has hackeado el sistema!\n")
            print("¡Has completado el Nivel 3!\n")
            return True
        else:
            print("Contraseña incorrecta.")

    print("Has agotado todos tus intentos. Inténtalo de nuevo más tarde.\n")
    return False

# Función principal del juego
def main():
    intro()
    
    if level_1():
        if level_2():
            if not level_3():
                print("¡Mejor suerte la próxima vez!")

if __name__ == "__main__":
    main()