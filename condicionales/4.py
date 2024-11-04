# 4. Algoritmo que solicita Ingresos y Gastos y dice si ha habido beneficio o pérdida
def ejercicio4(args):
    ingresos = float(input("Introduce los ingresos: "))
    gastos = float(input("Introduce los gastos: "))
    if ingresos > gastos:
        print("Ha habido un beneficio.")
    elif ingresos < gastos:
        print("Ha habido una pérdida.")
    else:
        print("No ha habido ni beneficio ni pérdida.")
        
if __name__ == '__main__':
        import sys
        sys.exit(ejercicio4(sys.argv))