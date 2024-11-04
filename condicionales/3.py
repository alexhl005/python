# 3. Algoritmo que lee dos números y dice si son iguales o distintos
def ejercicio3(args):
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if num1 == num2:
        print("Los números son iguales.")
    else:
        print("Los números son distintos.")
        
if __name__ == '__main__':
        import sys
        sys.exit(ejercicio3(sys.argv))