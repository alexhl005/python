# 6. Algoritmo que lee dos números y los suma si ambos son negativos
def ejercicio6(args):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if num1 < 0 and num2 < 0:
        suma = num1 + num2
        print(f"La suma de los números es: {suma}")
    else:
        print("Ambos números no son negativos, no se realiza la suma.")
        
if __name__ == '__main__':
        import sys
        sys.exit(ejercicio6(sys.argv))