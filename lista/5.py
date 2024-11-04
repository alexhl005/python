#5. Igual que el anterior pero las asignaturas las introduce el usuario. 
from decimal import Decimal
from operator import itemgetter
import sys

def main(args):
    lista = []

    # Pedir al usuario que introduzca asignaturas y notas
    print("Introduce 5 asignaturas y sus notas:")
    for _ in range(5):
        asignatura = input("Nombre de la asignatura: ")
        nota = Decimal(input("Nota de la asignatura: "))
        lista.append((asignatura, nota))
    
    # Ordena la lista por la nota (índice 1 de cada tupla)
    lista_ordenada = sorted(lista, key=itemgetter(1))
    
    # Muestra la lista ordenada
    print("Asignaturas ordenadas por nota:")
    for asignatura, nota in lista_ordenada:
        print(f"{asignatura} --- {nota}")
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
