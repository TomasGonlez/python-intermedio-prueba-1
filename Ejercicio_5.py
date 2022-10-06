#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.
def IVA(cantidad,porcentaje):
    if porcentaje == "":
        total= cantidad+cantidad * 0.19
    else:
        porcentaje = float(porcentaje)/100
        total=cantidad+cantidad*porcentaje
    print("Factura total despues de aplicarle el porcentaje de IVA: "+str(total))
def main():
    iva = float(input("Ingrese cantidad para calcular el IVA: "))
    por_aplicar = input("Ingrese el porcentaje para calcular el IVA: ")
    IVA(iva,por_aplicar)

if __name__ == "__main__":
    main()