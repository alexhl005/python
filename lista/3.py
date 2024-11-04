#1. Crear una lista de 5 asignaturas y mostrarlas ordenadas alfabéticamente. 
from decimal import Decimal
def main(args):
    lista = [("ASGBD",Decimal(6.4)),("HLC",Decimal(9)),("SER",Decimal(8.5)),("ASO",Decimal(7.5)),("AIW",Decimal(8))]
    for i in lista:
        print(i)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))