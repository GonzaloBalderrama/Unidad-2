from Menu import Menu
from Manejador import ManejadorRegistro as manejador
if __name__=='__main__':
    menu=Menu()
    salir=False
    while not salir:
        print('1.Mostrar para cada variable el día y hora de menor y mayor valor')
        print('2.Indicar la temperatura promedio mensual por cada hora')
        print('3.Dado el dia listar hora, temperatura y presion')
        print('4.Salir')
        op=input('->')
        menu.opcion(op,manejador)
        salir = op =='4'