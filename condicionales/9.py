# 9. Algoritmo que pide tres números al usuario y los muestra ordenados de mayor a menor
def ejercicio9(args):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))
    
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    
    print("Números ordenados de mayor a menor:", numeros)

if __name__ == '__main__':
        import sys
        sys.exit(ejercicio9(sys.argv))