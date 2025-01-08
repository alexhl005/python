def main(args):
    lista = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n"]
    f = open("prueba.txt", "a")
    f.writelines(lista)
    f.close()

    r = open("prueba.txt", "r")
    print(r.read())
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))