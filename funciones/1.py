#def 1
def equipo(ip):
    contador = 0
    for i in range(len(ip)):
        for j in range(len(ip[i])):
            if ip[i][j] == ".":
                contador += 1
        if contador == 3:
            return(ip[i])

def main(args):
    usuario = ("alex", "asir05", "192.168.8.15")
    ip=equipo(usuario)
    print(ip)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))