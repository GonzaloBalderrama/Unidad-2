import csv
from PlanAhorro import PlanAhorro

class ManejadorPA:
    def __init__(self):
        self.__listaPA = []

    def __str__(self):
        s = ""
        for plan in self.__listaPA:
            s += str(plan) + '\n'
        return s

    def agregarPA(self, unPA):
        self.__listaPA.append(unPA)

    def crearPA(self):
        archivo = open("planes.csv")
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            unPA = PlanAhorro(int(fila[0]), fila[1], fila[2], int(fila[3]))
            self.agregarPA(unPA)
        archivo.close()