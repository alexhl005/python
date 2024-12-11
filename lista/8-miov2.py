def construir_datos():
    num_alumnos = int(input("Introduce el número de alumnos: "))
    lista = []
    
    for i in range(num_alumnos):
        lista_alumno = []
        alumno = input("Introduce el nombre del alumno: ")
        lista_alumno.append((i + 1, alumno))
        num_asignaturas = int(input("Introduce el número de asignaturas: "))
        for _ in range(num_asignaturas):
            asignatura = input("Introduce el nombre de la asignatura: ")
            nota = int(input(f"Introduce la nota de {asignatura}: "))
            lista_alumno.append((asignatura, nota))
        lista.append(lista_alumno)

    return lista

def mostrar_datos(lista):
    for alumno in lista:
        print(f"\nAlumno {alumno[0][0]}: {alumno[0][1]}")
        for asignatura, nota in alumno[1:]:
            print(f"  Asignatura: {asignatura}, Nota: {nota}")

def calcular_media_y_maxima(lista):
    for alumno in lista:
        notas = [nota for _, nota in alumno[1:]]
        media = sum(notas) / len(notas)
        maxima = max(notas)
        print(f"\nAlumno {alumno[0][1]}:")
        print(f"  Nota media: {media:.2f}")
        print(f"  Nota máxima: {maxima}")

def main():
    lista = construir_datos()
    print("\nMostrando datos de los alumnos:")
    mostrar_datos(lista)
    print("\nCalculando media y nota máxima:")
    calcular_media_y_maxima(lista)

if __name__ == '__main__':
    main()
