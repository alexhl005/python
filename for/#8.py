#8. Diseñar un algoritmo que muestra el factorial de un número pedido al usuario. El número debe ser mayor de 0.
def main(args):
    num = int(input("Introduce el numero que deseada factorial: "))
    resultado = 1
    for i in range(1,num+1):
        resultado = resultado * i
    print(resultado)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))