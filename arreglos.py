def alreves(nombre):
    nombre_al_reves_resultado = ""
    longitud = len(nombre)
    for i in range(longitud):
        nombre_al_reves_resultado += nombre[longitud - i - 1]
    return nombre_al_reves_resultado

def cantidadletras(nombre):
    cantidad_letras_resultado = len(nombre)
    return cantidad_letras_resultado