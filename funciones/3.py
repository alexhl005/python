#def 1
def menu():
        print("1. Sumar")
        print("2. Restar")    
        print("3. Multipilcar")
        op=int(input("Elija una opción: "))
        return op
    
def main(args):
    op=menu()
    num1=int(input("Introduzca el primer numero: "))
    num2=int(input("Introduzca el segundo numero: "))
    while op==0 or op>3:
        print("operación no válida")
        op=menu()
    
    match (op):
        case (1):
            resultado=num1 + num2
            print (resultado)
        case (2):
            if num1 < num2:
                t = num1
                num1 = num2
                num2 = t
                resultado=num1 - num2
                print (resultado)
        case (3):
            resultado=num1 * num2
            print (resultado)
    # end match
    
        
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))