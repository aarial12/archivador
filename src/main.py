#import su respectiva funcion 

def printMenu():
    print("Menu de acciones:")
    print("1 Crear un directorio\n2 Crear un archivo de texto\n3 Escribir informacion en un archivo\n4 Leer el contenido de un archivo \n5 Renombrar un archivo \n6 Copiar un archivo \n7 Eliminar un archivo \n8 Listar archivos de un directorio \n9 Consultar informacion de un archivo \n0 Salir")

def main():
    while True:
        printMenu()
    
        accion = int (input())
        
        #Recuerden borrar el continue cuando coloquen su funcion
        match accion:
            case 1:
                continue
                #Funcion
            case 2:
                continue
                #Funcion
            case 3:
                continue
                #Funcion
            case 4:
                continue
                #Funcion
            case 5:
                continue
                #Funcion
            case 6:
                continue
                #Funcion
            case 7:
                continue
                #Funcion
            case 8:
                continue
                #Funcion
            case 9:
                continue
                #Funcion
            case 0:
                break
                
            case _:
                print("La entrada debe ser un numero del 1 al 0.")
    


main()
