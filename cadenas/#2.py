#2. Contar los espacios en blanco de una cadena de caracteres introducida por teclado.
def main(args):
    cadena = input("Escribe una cadena de texto: ")
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == " ":
            contador = contador + 1
    print(contador)
        

    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
