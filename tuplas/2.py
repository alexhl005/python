def main(args):
    pc1 = ("asir01", ("usuario1", "antonio", "root"))
    
    for i in range(len(pc1)):
        # Verificamos si el elemento es una cadena
        if type(pc1[i]) == str:
            print(pc1[i])
        else:
            # Si no es una cadena, asumimos que es una tupla y la iteramos
            for dato in pc1[i]:
                print(dato)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))