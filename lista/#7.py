#6
from decimal import Decimal

def main(args):
    lista = [(("ASGBD", Decimal(6.5)), ("HLC", Decimal(9))),(("SER", Decimal(8.5)), ("ASO", Decimal(7.5))),(("AIW", Decimal(8)), ("ASGBD", Decimal(6.5)))]
    print("ASIGNATURAS")
    print("=============================")
    for i in range(len(lista)):
        print("Alumno", i + 1)
        total = Decimal(0)  # Inicializamos el total en Decimal
        for j in range(len(lista[i])):
            print(lista[i][j][0], "---", lista[i][j][1])
            total += lista[i][j][1]  # Suma las notas
        media = total / 2  # Calcula la media
        print("La media del alumno es:", media)

    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
