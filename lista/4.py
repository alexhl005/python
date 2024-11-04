#4. Crear una lista de 5 asignaturas con sus notas y mostrarlas ordenadas por nota. Puedes hacer una ampliación de este ejercicio mostrando los datos de forma más legible.
from decimal import Decimal
from operator import itemgetter

def main(args):
    lista = [("ASGBD", Decimal(6.5)), ("HLC", Decimal(9)), ("SER", Decimal(8.5)), ("ASO", Decimal(7.5)), ("AIW", Decimal(8))]
    
    # Ordena la lista por la nota (índice 1 de cada tupla)
    lista_ordenada = sorted(lista, key=itemgetter(1))
    
    # Muestra la lista ordenada
    print("Asignaturas ordenadas por nota:")
    for asignatura, nota in lista_ordenada:
        print(f"{asignatura} --- {nota}")
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
