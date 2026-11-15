import os
def crearDirectorio(nombre):
    try:
        os.mkdir("../explorador/"+nombre); #Desde dentro de src
    except FileNotFoundError:
        os.mkdir("explorador/"+nombre); #Fuera de src
    print("Directorio", nombre, "creado");
