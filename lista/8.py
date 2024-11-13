from decimal import Decimal

def calcular_total_y_media(asignaturas):
    total_notas = sum(nota for _, nota in asignaturas)
    promedio_notas = total_notas / len(asignaturas)
    return total_notas, promedio_notas

def mostrar_notas(alumno_numero, asignaturas):
    print(f"\nAlumno {alumno_numero}:")
    for nombre_asignatura, nota_asignatura in asignaturas:
        print(f"{nombre_asignatura} --- {nota_asignatura}")

def main():
    lista_alumnos = []
    todas_las_notas = []

    # Pedir el número de alumnos
    num_alumnos = int(input("Introduce el número de alumnos: "))

    # Recoger las asignaturas y notas de cada alumno
    for alumno_numero in range(1, num_alumnos + 1):
        print(f"\nIntroduce las asignaturas y notas del alumno {alumno_numero}:")
        asignaturas = []
        
        num_asignaturas = int(input("Introduce el número de asignaturas: "))
        
        for _ in range(num_asignaturas):
            asignatura = input("Nombre de la asignatura: ")
            nota = Decimal(input("Nota de la asignatura: "))
            asignaturas.append((asignatura, nota))
            todas_las_notas.append(nota)  # Guardar cada nota en una lista general para después hallar la nota más alta
        
        lista_alumnos.append(asignaturas)

    # Mostrar notas, media de cada alumno y calcular la nota más alta de todos
    for alumno_numero, asignaturas_alumno in enumerate(lista_alumnos, start=1):
        mostrar_notas(alumno_numero, asignaturas_alumno)
        _, promedio = calcular_total_y_media(asignaturas_alumno)
        print(f"La media del alumno {alumno_numero} es: {promedio}")

    # Calcular y mostrar la nota más alta entre todos los alumnos
    nota_mas_alta_global = max(todas_las_notas)
    print(f"\nLa nota más alta entre todos los alumnos es: {nota_mas_alta_global}")

if __name__ == '__main__':
    main()
