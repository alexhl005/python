# 8. Algoritmo que pide tres números al usuario y decide cuál es el mayor
def ejercicio8(args):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))
    
    mayor = max(num1, num2, num3)
    print(f"El número mayor es: {mayor}")

if __name__ == '__main__':
        import sys
        sys.exit(ejercicio8(sys.argv))