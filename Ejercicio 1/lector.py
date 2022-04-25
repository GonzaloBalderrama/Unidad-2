import csv
from Email import Email

class ManejadorEmail:
    def __init__(self):
        self.__listaEmails = []

    def agregarEmail(self, unEmail):
        self.__listaEmails.append(unEmail)

    def crearEmail(self):
        archivo = open('emails.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            unEmail = Email(fila[0], fila[1], fila[2], fila[3])
            self.agregarEmail(unEmail)
        archivo.close()

    def mostrarLista(self):
