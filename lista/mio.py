from decimal import Decimal

def main(args):
    lista = [(("ASGBD",Decimal(6.5)),("HLC",Decimal(9))),(("SER",Decimal(8.5)),("ASO",Decimal(7.5))),(("AIW",Decimal(8)),("ASGBD",Decimal(6.5)))]
    for i in range(len(lista)):
        print("Alumno",i + 1)
        suma = Decimal(0)
        for j in range(len(lista[i])):
            print(lista[i][j][0],"---",lista[i][j][1])
            suma += lista[i][j][1]
        media = suma / 2
        print("La media del alumno es: ",media)
        
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
