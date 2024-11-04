# 7. Algoritmo que presenta un menú al usuario con las operaciones de suma, resta y multiplicación
def ejercicio7(args):
    print("Menú de operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    
    opcion = int(input("Elige una opción (1, 2 o 3): "))
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    if opcion == 1:
        print(f"Resultado de la suma: {num1 + num2}")
    elif opcion == 2:
        print(f"Resultado de la resta: {num1 - num2}")
    elif opcion == 3:
        print(f"Resultado de la multiplicación: {num1 * num2}")
    else:
        print("Opción no válida.")
        
if __name__ == '__main__':
        import sys
        sys.exit(ejercicio7(sys.argv))