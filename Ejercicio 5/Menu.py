from ManejadorPA import ManejadorPA
from PlanAhorro import PlanAhorro

class Menu:
    def opcion(self, lista):
        salir=False
        while not salir:
            print('1.Actualizar el valor del vehículo de cada plan')
            print('2.Buscar por precio')
            print('3.Mostrar monto a pagar para licitar')
            print('4.Mostrar cantidad de cuotas para licitar')
            print('5.Salir')
            op=input('Opcion-->')
            salir = op =='5'