#1. Crear una lista de 5 asignaturas y mostrarlas ordenadas alfabéticamente. 
def main(args):
    lista = ["ASGBD","HLC","SER","ASO","AIW"]
    lista.sort()
    print(lista)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))