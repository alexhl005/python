def mostrarDatos(diccionario):
    for servidor in diccionario:
        print(f"{servidor}")
        for clave,valor in diccionario[servidor].items():
            if clave != "DNS":
                print(f"\t{clave} --- {valor}")
            else:
                print(f"\t{clave}")
                for datos in valor:
                    print(f"\t\t{datos}")

def introducirDatos():
    datos = {}
    numServ = int(input("Cuantos servidores necesitas añadir: "))
    for _servidor in range(numServ):
        nameServer = input("Introduce el nombre del servidor: ")
        ips = input(f"Introduce la ip del servidor {nameServer}: ")
        mascara = input(f"Introduce la mascara para la ip {ips}: ")
        gateway = input(f"Introduce la puerta de enlace de el servidor {nameServer}: ")
        dnss = []
        numDNS = int(input("Cuantos DNS's necesitas añadir: "))
        for i in range(numDNS):
            nameDns = input(f"Introduce el DNS {i + 1}: ")
            dnss.append(nameDns)
        datos.update({nameServer:{"ip":ips,"mascara":mascara,"gateway":gateway,"DNS":dnss}})
    return datos

def main(args):
    datos = {
        'Serv1': {
            "ip":"192.168.8.1",
            "mascara":"255.255.255.0", 
            "gateway":"192.168.8.1",
            "DNS": ["8.8.8.8","8.8.4.4","192.168.8.1"],
        },
        'Serv2': {
            "ip":"192.168.9.1",
            "mascara":"255.255.255.0", 
            "gateway":"192.168.9.1",
            "DNS": ["208.67.222.222","208.67.220.220"],
        }
    }
    #mostrarDatos(datos)
    introducirDatos()
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
