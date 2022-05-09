from menu import Menu
from manejador import Manejador
if __name__=='__main__':
    menu=Menu()
    manejador=Manejador()
    salir=False
    band=0
    while not salir:
        print('------------------------------------------')
        print('1.Actualizar el valor del vehículo de cada plan')
        print('2.Mostrar codigo del plan, modelo y version del vehiculo, ingresando un valor')
        print('3.Mostrar monto que se debe haber pagado para licitar un vehiculo')
        print('4.Ingresando un codigo, Modificar la cantidad de cuotas que deben tener pagas para licitar')
        print('5.Salir')
        print('------------------------------------------')
        op=input('->')
        if band != -1:
                manejador.leerArchivo()
                band=-1
        menu.opcion(op,manejador)
        salir = op =='5'