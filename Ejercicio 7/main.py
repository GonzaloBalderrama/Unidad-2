import csv
from re import M
from ViajeroFrecuente import ViajeroFrecuente

if __name__ == '__main__':
    lista = []

    archivo = open('viajeros.csv')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        unViajero = ViajeroFrecuente(int(fila[0]), int(fila[1]), fila[2], fila[3], int(fila[4]))
        lista.append(unViajero)
        print(fila)
    archivo.close()

    print("\n****Sobrecarga del operador relacional mayor****")
    max = 0
    i=0
    for fila in lista:
        if fila>lista[max]:
            max = i
        i +=1
    print(f"El viajero con mayor cantidad de millas es: {lista[max].getNombre()}")
    
    print("\n****Sobrecarga del operador suma por izquierda****")
    print(f"Viajero: {lista[0].getNombre()}   Cantidad de millas: {lista[0].cantidadTotaldeMillas()}")
    numero = int(input("Ingrese la cantidad de millas a sumar: "))
    print(f"Millas actualizadas: {lista[0]+numero}")

    print("\n****Sobrecarga del operador resta por izquierda****")
    print(f"Viajero: {lista[1].getNombre()}   Cantidad de millas: {lista[1].cantidadTotaldeMillas()}")
    numero = int(input("Ingrese la cantidad de millas a canjear: "))
    print(f"Millas actualizadas: {lista[1]-numero}")

    print("\n****Sobrecarga del operador igual por izquierda****")
    print(f"Viajero: {lista[0].getNombre()}   Cantidad de millas: {lista[0].cantidadTotaldeMillas()}")
    numero = int(input("Ingrese la cantidad de millas a comparar: "))
    if lista[0] == numero:
        print("Las cantidades son iguales")
    else: 
        print("Las cantidades son diferentes")

    print("\n****Sobrecarga del operador igual por derecha****")
    print(f"Viajero: {lista[0].getNombre()}   Cantidad de millas: {lista[0].cantidadTotaldeMillas()}")
    numero = int(input("Ingrese la cantidad de millas a comparar: "))
    if numero == lista[0]:
        print("Las cantidades son iguales")
    else: 
        print("Las cantidades son diferentes")

    print("\n****Sobrecarga del operador suma por derecha****")
    print(f"Viajero: {lista[0].getNombre()}   Cantidad de millas: {lista[0].cantidadTotaldeMillas()}")
    numero = int(input("Ingrese la cantidad de millas a sumar: "))
    print(f"Millas actualizadas: {numero+lista[0]}")

    print("\n****Sobrecarga del operador resta por derecha****")
    print(f"Viajero: {lista[1].getNombre()}   Cantidad de millas: {lista[1].cantidadTotaldeMillas()}")
    numero = int(input("Ingrese la cantidad de millas a canjear: "))
    print(f"Millas actualizadas: {numero-lista[1]}")