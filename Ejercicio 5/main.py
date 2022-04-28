from ManejadorPA import ManejadorPA
from Menu import Menu
from PlanAhorro import PlanAhorro

if __name__ == "__main__":
    lista = ManejadorPA()
    lista.crearPA()
    print(lista)
    menu=Menu()
    menu.opcion()