#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lenguaje) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
def main():
    lista = ["Matemáticas", "Física","Química", "Historia" ,"Lenguaje"]
    largo = len(lista) - 1
    for asignatura in lista[::-1]:
        nota = input("Ingrese su nota para "+asignatura+": ")
        nota = nota.replace('.','')
        nota = int(nota)
        print("Su nota es "+ str(nota))
        if(nota >= 40):
            lista.remove(asignatura)     
    return lista
        
if __name__ == "__main__":
    a= main()
    print("Los ramos que debe repetir son: "+str(a))