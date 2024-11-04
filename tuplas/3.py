def main(args):
    pc1 = (("usuario1", "Pepe", "Rodriguez", "988554411", "pepe.rodriguez@gmail.com"),
           ("usuario2", "Rafa", "Bello", "698754123", "rafa.bello@gmail.com"),"root")
    
    for usuario in pc1:
        # Verificamos si el elemento es una tupla
        if isinstance(usuario, tuple):
            # Imprimimos los datos del usuario
            print(f"{usuario[0]}: Nombre: {usuario[1]}, Apellido: {usuario[2]}, Teléfono: {usuario[3]}, Correo: {usuario[4]}")
        else:
            print(usuario)  # En caso de que haya un elemento que no sea tupla

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))