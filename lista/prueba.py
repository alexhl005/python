from decimal import Decimal
def avg(asignatura):
    for i in range(len(asignatura)):
        total = Decimal(0)
        for j in range(len(asignatura[i])):
            total = total + asignatura[i][j][1]
        media = total / 2
        return(media)

def main():
    lista_alumnos = [
        [("ASGBD", Decimal(6.5)), ("HLC", Decimal(9))],
        [("SER", Decimal(8.5)), ("ASO", Decimal(7.5))],
        [("AIW", Decimal(8)), ("ASGBD", Decimal(6.5))]
    ]
    avg(lista_alumnos)


if __name__ == '__main__':
    main()