from Medicamento import Medicamento
import csv

class ManejadorMedicamento:
    __listaM = []
    
    def __init__(self):
        self.__listaM = []

    def __str__(self):
        s = ""
        for medicamento in self.__listaM:
            s += str(medicamento) + '\n'
        return s

    def agregarM(self, unM):
        self.__listaM.append(unM)

    def crearM(self):
        archivo = open("medicamentos.csv")
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                unM = Medicamento(int(fila[0]), int(fila[1]), fila[2], fila[3], fila[4], fila[5], int(fila[6]))
                self.agregarM(unM)
        archivo.close()
        
    def buscarMedicamentos(self, hab):
        total = 0
        print("\nMedicamento/monodroga      Presentacion       Cantidad       Precio")
        for fila, medicamentos in enumerate(self.__listaM): 
            if medicamentos.getIdCama() == hab:
                print(f"{medicamentos.getNombre()}/{medicamentos.getMonodroga()}         {medicamentos.getPresentacion()}         {medicamentos.getCantidad()}         ${medicamentos.getPrecio()}")
                total += int(medicamentos.getPrecio())
        print(f"Total                                                        ${total}")