import csv
from Email import Email

class ManejadorEmail:
    def __init__(self):
        self.__listaEmails = []

    def __str__(self):
        s = ""
        for email in self.__listaEmails:
            s += str(email) + '\n'
        return s

    def agregarEmail(self, unEmail):
        self.__listaEmails.append(unEmail)

    def crearEmail(self):
        archivo = open("emails.csv")
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            unEmail = Email(fila[0], fila[1], fila[2], fila[3])
            self.agregarEmail(unEmail)
        archivo.close()

    def buscarEmail(self):
        buscar = input("Ingrese el Id que desea buscar: ")
        contador = 0
        for lista, email in enumerate(self.__listaEmails):
            if email.getID() == buscar:
                contador += 1
        print(f"El ID ingresado se repite {contador} veces")