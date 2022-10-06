#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
#Aclaración: El programa debe imprimir por la consola el mismo texto que el usuario introduce hasta que éste escriba la palabra "salir".
def main():
    eco = ""
    while eco != "salir":
        eco = input("Introduce texto: ")
        print("FINALIZO EL PROGRAMA")

if __name__ == "__main__":
    main()