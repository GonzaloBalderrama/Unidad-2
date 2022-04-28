import csv
from ViajeroFrecuente import ViajeroFrecuente
from menu import menu

if __name__ == '__main__':
    lista = []
    numviajero = 0
    ban = False
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        unViajero = ViajeroFrecuente(int(fila[0]), int(fila[1]), fila[2], fila[3], float(fila[4]))
        lista.append(unViajero)
    archivo.close()

    numviajero = int(input("Ingrese el numero del viajero: "))
    i = 0
    while ban == False and i<len(lista):
        unViajero = lista[i]
        if unViajero.getNumero() == numviajero:
            print("Viajero encontrado")
            ban = True
        else:
            i += 1
    
    if ban == False:
        print("Viajero no encontrado")
        exit()
    
    opcion = 0    
    while opcion != 5:
        print("************************************************** MENU **************************************************")
        print("1 - Consultar cantidad de millas")
        print("2 - Acumular millas")
        print("3 - Canjear millas")
        print("4 - Salir")
        print("**********************************************************************************************************")
        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            print(f"Cantidad de millas: {unViajero.cantidadTotaldeMillas()}")
        elif opcion == 2:
            nuevas_millas = float(input("Ingrese la cantidad de millas a sumar: "))
            unViajero.acumularMillas(nuevas_millas)
        elif opcion == 3:
            cant_millas = float(input("Ingrese la cantidad de millas a canjear: "))
            unViajero.canjearMillas(cant_millas)
        elif opcion == 4:
            exit()
        else:
            print("La opción ingresada es incorrecta")

