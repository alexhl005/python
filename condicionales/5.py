# 5. Algoritmo que lee dos números y los suma si alguno de ellos es positivo
def ejercicio5(args):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if num1 > 0 or num2 > 0:
        suma = num1 + num2
        print(f"La suma de los números es: {suma}")
    else:
        print("Ninguno de los números es positivo, no se realiza la suma.")
        
if __name__ == '__main__':
        import sys
        sys.exit(ejercicio5(sys.argv))