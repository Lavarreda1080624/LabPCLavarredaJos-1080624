def menu_principal():
    cursos = [] #Estos tres arreglos vacios se usan para ingresar la informacion del usuario
    alumnos = []
    notas = []

    while True:
        print("Este sistema es de cursos y notas(URL proyecto)")
        print("Qué desea hacer el día de hoy?:)",
              "1. Creación o edición de curso",
              "2. Control y creación de alumnos",
              "3. Calificación de cursos",
              "4. Reportes de alumnos",
              "5. SALIR", sep="\n")
        opcion = input("Ingrese su opción monami: ")

        match opcion:
            case '1':
                gestionar_cursos(cursos)
            case '2':
                gestionar_alumnos(alumnos)
            case '3':
                gestionar_notas(cursos, alumnos, notas)
            case '4':
                generar_reportes(cursos, alumnos, notas)
            case '5':
                print("Esta saliendo del programa, que le vaya bien ;)")
                break
            case _:
                print("Seleccione una opcion que si le dije que podia ingresar por favor")

def gestionar_cursos(cursos):
    while True:
        print("1. Agregar un curso", "2. Editar el o los cursos", "3. Salir", sep="\n")
        opcionc = input("Ingrese su opción: ")

        match opcionc:
            case '1':
                agregar_curso(cursos)
            case '2':
                editar_curso(cursos)
            case '3':
                print("Salir al menu principal")
                break
            case _:
                print("Esta opcion no es valida, elija una que si lo sea.")
        print("Lista de cursos:")
        for curso in cursos:
            print(curso)

def agregar_curso(cursos):
    id_curso = int(input("Ingrese el ID del curso (Solo se admitiran numero enteros): "))
    nombre_curso = input("Ingrese el nombre del curso: ")
    horario_curso = input("Ingrese el horario del curso: ")
    salon_curso = input("Ingrese el salón del curso: ")
    catedratico_curso = input("Ingrese el catedrático del curso: ")

    curso_existente = any(curso["ID"] == id_curso for curso in cursos) #Este any que se ve se usa como "al menos" como que si al menos uno de los cursos
    if curso_existente:
        print("Ya existe un curso con este ID.")
    else:
        curso = {
            "ID": id_curso,
            "Nombre": nombre_curso,
            "Horario": horario_curso,
            "Salón": salon_curso,
            "Catedrático": catedratico_curso
        }
        cursos.append(curso)
        print("Curso agregado exitosamente.")

def editar_curso(cursos):
    buscador_cursos = int(input("Ingrese el ID del curso que desea editar: "))
    curso = next((curso for curso in cursos if curso["ID"] == buscador_cursos), None) #El none indica la ausencia de un valor
    if curso:
        print("Curso encontrado: Por favor, ingrese los nuevos datos:")
        curso["Nombre"] = input("Nuevo nombre del curso: ")
        curso["Horario"] = input("Nuevo horario del curso: ")
        curso["Salón"] = input("Nuevo salón del curso: ")
        curso["Catedrático"] = input("Nuevo catedrático del curso: ")
        print("Curso editado exitosamente.")
    else:
        print("El curso que usted solicita no existe, si desea crear unocambie de opción")

def gestionar_alumnos(alumnos):
    while True:
        print("1. Agregar alumno", "2. Editar alumno", "3. Salir", sep="\n")
        opciona = input("Ingrese su opción: ")

        match opciona:
            case '1':
                agregar_alumno(alumnos)
            case '2':
                editar_alumno(alumnos)
            case '3':
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Por favor, elija una opción que si lo sea.")
        print("Lista de alumnos:")
        for alumno in alumnos:
            print(alumno)

def agregar_alumno(alumnos):
    carne = int(input("Ingrese el carné del alumno: "))
    nombre = input("Ingrese el nombre del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")

    alumno_existente = any(alumno["Carné"] == carne for alumno in alumnos)
    if alumno_existente:
        print("Ya existe un alumno con este carné.")
    else:
        alumno = {
            "Carné": carne,
            "Nombre": nombre,
            "Fecha de Nacimiento": fecha_nacimiento
        }
        alumnos.append(alumno)
        print("Alumno agregado exitosamente.")

def editar_alumno(alumnos):
    buscador_alumnos = int(input("Ingrese el carné del alumno que desea buscar: "))
    alumno = next((alumno for alumno in alumnos if alumno["Carné"] == buscador_alumnos), None)
    if alumno:
        print("Alumno encontrado, ingrese los nuevos datos:")
        alumno["Nombre"] = input("Nuevo nombre del alumno: ")
        alumno["Fecha de Nacimiento"] = input("Nueva fecha de nacimiento del alumno (DD/MM/AAAA): ")
        print("Alumno exitosamente agregado.")
    else:
        print("Este alumno no existe, cuidado")

def gestionar_notas(cursos, alumnos, notas):
    while True:
        print("1. Agregar notas a un alumno", "2. Revisar notas de los alumnos", "3. Salir", sep="\n")
        opcionn = input("Ingrese su opción: ")

        match opcionn:
            case '1':
                agregar_nota(cursos, alumnos, notas)
            case '2':
                revisar_notas(notas)
            case '3':
                print("Ir al menu principal")
                break
            case _:
                print("Opción no válida. Por favor, elija una opción que si sea válida.")

def agregar_nota(cursos, alumnos, notas):
    carne_notas = int(input("Ingrese el carné del alumno al que desea agregarle notas: "))
    curso_nota = int(input("Ingrese el ID del curso: "))
    nota_alumno = int(input("¿Qué nota obtuvo el alumno?:) "))

    curso_existente = any(curso["ID"] == curso_nota for curso in cursos)
    alumno_existente = any(alumno["Carné"] == carne_notas for alumno in alumnos)

    if curso_existente and alumno_existente:
        nota = {
            "Carné": carne_notas,
            "IDCurso": curso_nota,
            "Nota": nota_alumno
        }
        notas.append(nota)
        print("Nota agregada correctamente.")
    else:
        if not curso_existente:
            print("Este curso no existe, por favor si asi desea cree uno.")
        if not alumno_existente:
            print("Este alumno no existe, si desea ejecutar esta acción cree uno.")

def revisar_notas(notas):
    buscador_notas = int(input("Ingrese el ID del alumno del que desea ver las notas: "))
    notas_alumno = [nota for nota in notas if nota["Carné"] == buscador_notas]
    if notas_alumno:
        print(f"Notas del alumno con carné {buscador_notas}:")
        for nota in notas_alumno:
            print(nota)
    else:
        print("No hay notas registradas para este alumno.")

def generar_reportes(cursos, alumnos, notas):
    while True:
        print("Qué reporte desea ver amigo mio?:",
              "a. Cursos y número de estudiantes",
              "b. Notas de estudiantes de curso seleccionado",
              "c. Notas de estudiante",
              "d. Reportes de los alumnos",
              "e. Nota media por curso",
              "f. Estudiante con mejor desempeño",
              "g. Salir", sep="\n")
        opcionr = input("Ingrese su opción: ")

        match opcionr:
            case 'a':
                reporte_cursos_estudiantes(cursos, notas)
            case 'b':
                reporte_notas_curso(notas)
            case 'c':
                reporte_notas_alumno(notas)
            case 'd':
                reporte_alumnos_notas(alumnos, notas)
            case 'e':
                reporte_nota_media(cursos, notas)
            case 'f':
                reporte_mejor_desempeno(alumnos, cursos, notas)
            case 'g':
                print("Saliendo de reportes...")
                break
            case _:
                print("Opción no válida. Por favor, elija una opción válida.")

def reporte_cursos_estudiantes(cursos, notas):
    for curso in cursos:
        num_estudiantes = sum(1 for nota in notas if nota["IDCurso"] == curso["ID"])
        print(f"Curso: {curso['Nombre']}, Número de estudiantes: {num_estudiantes}")

def reporte_notas_curso(notas):
    curso_id = int(input("Ingrese el ID del curso: "))
    notas_curso = [nota for nota in notas if nota["IDCurso"] == curso_id]
    if notas_curso:
        print(f"Notas para el curso ID {curso_id}:")
        for nota in notas_curso:
            print(nota)
    else:
        print("No hay notas registradas para este curso.")

def reporte_notas_alumno(notas):
    carne_alumno = int(input("Ingrese el carné del alumno: "))
    notas_alumno = [nota for nota in notas if nota["Carné"] == carne_alumno]
    if notas_alumno:
        print(f"Notas del alumno con carné {carne_alumno}:")
        for nota in notas_alumno:
            print(nota)
    else:
        print("No hay notas registradas para este alumno.")

def reporte_alumnos_notas(alumnos, notas):
    print("Lista de alumnos y sus notas:")
    for alumno in alumnos:
        print(f"Alumno: {alumno['Nombre']}, Carné: {alumno['Carné']}")
        notas_alumno = [nota for nota in notas if nota["Carné"] == alumno["Carné"]]
        for nota in notas_alumno:
            print(nota)

def reporte_nota_media(cursos, notas):
    for curso in cursos:
        suma_notas = sum(nota["Nota"] for nota in notas if nota["IDCurso"] == curso["ID"])
        contador_notas = sum(1 for nota in notas if nota["IDCurso"] == curso["ID"])
        if contador_notas > 0:
            nota_media = suma_notas / contador_notas
            print(f"Curso: {curso['Nombre']}, Nota media: {nota_media:.2f}")
        else:
            print(f"Curso: {curso['Nombre']}, No hay notas registradas.")

def reporte_mejor_desempeno(alumnos, cursos, notas):
    mejor_desempeno = None
    mayor_nota = -1

    for nota in notas:
        if nota["Nota"] > mayor_nota:
            mayor_nota = nota["Nota"]
            mejor_desempeno = nota

    if mejor_desempeno:
        mejor_alumno = next((alumno for alumno in alumnos if alumno["Carné"] == mejor_desempeno["Carné"]), None)
        mejor_curso = next((curso for curso in cursos if curso["ID"] == mejor_desempeno["IDCurso"]), None)
        if mejor_alumno and mejor_curso:
            print(f"Mejor promedio: {mejor_alumno['Nombre']} con una nota de {mejor_desempeno['Nota']} en el curso {mejor_curso['Nombre']}")
        else:
            print("No se pudo encontrar el mejor desempeño.")
if __name__ == "main":
    menu_principal()