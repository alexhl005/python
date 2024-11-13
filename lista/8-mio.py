def construir_datos():
    num_alumnos = int(input("Introduce el número de alumnos: "))
    lista = []
    
    for i in range(num_alumnos):
        lista_alumno = []
        alumno = input("Introduce el nombre del alumno: ")
        lista_alumno.append((i + 1, alumno))
        num_asignaturas = int(input("Introduce el número de asignaturas: "))
        for j in range(num_asignaturas):
            asignatura = input("Introduce el nombre de la asignatura: ")
            nota = int(input(f"Introduce la nota de {asignatura}: "))
            lista_alumno.append((asignatura, nota))
        lista.append(lista_alumno)

    return lista

def main():
    datos = construir_datos()
    print(datos)

if __name__ == '__main__':
    main()
