#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: (IMAGEN ADJUNTA). 
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.
def main():
    renta = float(input("Ingrese renta anual: "))

    if renta < 10000:
        renta = renta *0.05
    elif renta < 20000:
        renta = renta *0.15
    elif renta < 35000:
        renta= renta*0.20
    elif renta < 60000:
        renta= renta * 0.30
    else:
        renta = renta * 0.45
    print("Usted debe pagar "+str(renta))

if __name__ == "__main__":
    main() 