#1. Crear una lista de 5 asignaturas y mostrarlas ordenadas alfabéticamente. 
def main(args):
    e1 = input("Introduce una asignatura: ")
    e2 = input("Introduce una asignatura: ")
    e3 = input("Introduce una asignatura: ")
    e4 = input("Introduce una asignatura: ")
    e5 = input("Introduce una asignatura: ")
    lista = [e1,e2,e3,e4,e5]
    lista.sort()
    print(lista)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))