import csv
import numpy as np
from Cama import Cama
from ManejadorMedicamento import ManejadorMedicamento

class ManejadorCama:
    __indice = 0
    __cantidad = 0
    def __init__(self):
        self.__listaC = np.empty(30, dtype=Cama)

    def __str__(self):
        s = ""
        i=0
        for cama in self.__listaC:
            if i<self.__cantidad:
                s += str(cama) + '\n'
                i += 1
        return s

    def agregarC(self, unaC):
        self.__listaC[self.__indice] = unaC
        self.__cantidad += 1

    def crearC(self):
        archivo = open("camas.csv")
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                unaC = Cama(int(fila[0]), fila[1], bool(fila[2]), fila[3], fila[4], fila[5], fila[6], fila[7])
                self.agregarC(unaC)
                self.__indice += 1
        archivo.close()

    def buscarPaciente(self, nom):
        i = 0
        while i < self.__cantidad and self.__listaC[i].getAyN()!=nom:
            i += 1
        if i<self.__cantidad:
            self.__listaC[i].actualizarAlta()
            print("\n***************************************************************************")
            print(f"Paciente: {self.__listaC[i].getAyN()}          Cama: {self.__listaC[i].getID()}          Habitacion: {self.__listaC[i].getHab()}")
            print(f"Diagnostico: {self.__listaC[i].getDiag()}          Fecha de internación: {self.__listaC[i].getFechaI()}")    
            print(f"Fecha de alta: {self.__listaC[i].getFechaA()}")  
            listamed = ManejadorMedicamento()
            listamed.crearM()
            listamed.buscarMedicamentos(self.__listaC[i].getID())
            print("***************************************************************************")

        else:
            print("Paciente no encontrado")

    def listarPorDiagnostico(self, diagnostico):
        i = 0
        print("\n***************************************************************************")
        while i<self.__cantidad:
            if self.__listaC[i].getDiag()==diagnostico:
                if self.__listaC[i].getEstado():
                    print(f"Paciente: {self.__listaC[i].getAyN()}          Cama: {self.__listaC[i].getID()}          Habitacion: {self.__listaC[i].getHab()}")
                    print(f"Diagnostico: {self.__listaC[i].getDiag()}          Fecha de internación: {self.__listaC[i].getFechaI()}\n\n")    
            i += 1
        print("***************************************************************************")