def mostrarDatos(datos):
    for servidor in datos:
        print(f"{servidor}")
        for clave,valor in datos[servidor].items():
            print(f"\t{clave} --- {valor}")

def introducirDatos():
    datos = {}
    numServ = int(input("Cuantos servidores necesitas añadir: "))
    for _servidor in range(numServ):
        nameServer = input("Introduce el nombre del servidor: ")
        numServices = int(input(f"Cuantos servicios vas a añadir para {nameServer}: "))
        servicios = {}
        for i in range(numServices):
            nameService = input(f"Introduce el nombre del servicio {i + 1}: ")
            numRam = int(input(f"Cuantos valores vas a añadir para {nameService}: "))
            valores = []
            for j in range(numRam):
                ram = input(f"Introduce el valor {j + 1}: ")
                valores.append(ram)
            servicios.update({nameService: valores})    
        datos.update({nameServer: servicios})

    return datos

def mediaServicios(datos):
    servidores = {}
    for servidor in datos:
        servicios = {}
        for claveServicio in datos[servidor]:
            total = 0
            for i in range(len(datos[servidor][claveServicio])):
                total = total + datos[servidor][claveServicio][i]
            media = total / len(datos[servidor][claveServicio])
            servicios.update({claveServicio: media})
        servidores.update({servidor: servicios})
    return servidores

def diccionarioMedias(media2):
    dicc = {}
    conteo = {}
    
    for servidor in media2:
        for claveServicio, media in media2[servidor].items():
            if claveServicio in dicc:
                dicc[claveServicio] += media
                conteo[claveServicio] += 1
            else:
                dicc[claveServicio] = media
                conteo[claveServicio] = 1
    
    for claveServicio in dicc:
        dicc[claveServicio] /= conteo[claveServicio]
    
    return dicc


def main(args):
    datos = {
 "SRV001": {
 "WebServer": [45, 32],
 "Database": [65],
 "BackupService": [98, 100, 96]
 },
 "SRV002": {
 "WebServer": [55, 60],
 "ApplicationServer": [75],
 "MonitoringTool": [89, 90]
 },
 "SRV003": {
 "FileStorage": [40, 42, 38],
 "LoggingService": [92]
 },
 "SRV004": {
 "MailServer": [50],
 "WebServer": [60, 65, 58],
 },
 "SRV005": {
 "Database": [70, 75],
 "BackupService": [100]
 }
}
    #datos = introducirDatos()
    #mostrarDatos(datos)
    #mediaServicios(datos)
    #mostrarDatos(serv)
    media2 = mediaServicios(datos)
    pitos = diccionarioMedias(media2)
    print(pitos)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
