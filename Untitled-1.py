print("Selecciona una opción:")
print("x. Opción A")
print("x. Opción B")
print("x. Opción C")

# Pedir al usuario que seleccione una opción
opcion = input("Marca con 'x' la opción que deseas: ")

# Manejar la selección del usuario
if opcion == 'x':
    print("Has seleccionado x.")
    # Aquí puedes realizar acciones adicionales según la opción seleccionada.
if opcion == 'y':
    print("Has seleccionado y.")
if opcion == 'z':
    print("Has seleccionado z.")
else:
    print("Selección no válida. Por favor, marca con 'x' una opción válida.")