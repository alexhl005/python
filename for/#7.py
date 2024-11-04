#7. Diseñar un algoritmo que muestre la tabla de multiplicar de un número que pide al usuario y que debe estar entre 1 y 10 (ambos inclusive).
def main(args):
    num = int(input("Introduce el numero de la tabla de multiplicar deseada: "))
    for i in range(11):
        resultado = num * i
        print("El resultado de multiplicar: ",i,"x",num,"=",resultado)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))