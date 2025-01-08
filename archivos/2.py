def main(args):
    lista = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n"]
    f = open("prueba3.txt", "w")
    for i in lista:
        f.write(i)
    f.close()

    r = open("prueba3.txt", "r")
    print(r.read())
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))