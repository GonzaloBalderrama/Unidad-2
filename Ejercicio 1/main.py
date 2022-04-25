from turtle import clear
from Email import Email
from ManejadorEmail import ManejadorEmail
import sys
from os import system

if __name__ == '__main__':
    ban = True
    unEmail = Email('gonzalo', 'gmail', 'com')
    unEmail.retornaEmail()
    while ban:
        print("------------------------------------------------------------------------------------------------------\n")
        print("1-Cargar emails de archivo")
        print("2-Buscar ID coincidentes")
        print("3-Ingresar email existente")
        print("4-Crear nuevo email")
        print("5-Cambiar contraseña")
        print("6-Salir")
        print("\n------------------------------------------------------------------------------------------------------")
        opcion = int(input("Ingrese la opción que desee: "))
        system("cls")
        if opcion == 1:
            lista = ManejadorEmail()
            lista.crearEmail()
            print("\nEstos son los correo obtenidos: ")
            print(lista)
        elif opcion ==2:
            lista.buscarEmail()
        elif opcion ==3:
            Email2 = Email()
            Email2.crearEmail()
        elif opcion == 4:
            Email1 = Email(input("Ingrese su Id: "), input('Ingrese dominio: '), input("Ingrese el tipo de dominio: "))
            nombre = input("Ingrese su nombre: ")
            print(f"\n Estimado/a {nombre} te enviaremos tus mensajes a la dirección {Email1.retornaEmail()}")
        elif opcion == 5:
            Email1.cambiarContrasenia()
        elif opcion == 6:
            sys.exit()

