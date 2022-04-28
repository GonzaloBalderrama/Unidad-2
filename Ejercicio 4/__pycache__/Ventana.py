from email.headerregistry import UniqueAddressHeader


class Ventana:
    __titulo = ""
    __xvsi = 0
    __yvsi = 0
    __xvid = 0
    __yvid = 0

    def __init__(self,titulo = "Defecto", xvsi = 0, yvsi = 0, xvid = 500, yvid = 500):
        self.__titulo = titulo
        self.__xvsi = xvsi
        self.__yvsi = yvsi
        self.__xvid = xvid
        self.__yvid = yvid

    def getTitulo(self):
        return self.__titulo
    
    def alto(self):
        return self.__xvid-self.__xvsi

    def ancho(self):
        return self.__yvid-self.__yvsi

    def mostrar(self):
        print(f"Titulo={self.__titulo}\nVertice superior izquierdo=({self.__xvsi},{self.__yvsi})\nVertice inferior derecho=({self.__xvid},{self.__yvid})\n")

    def subir(self, unidades=1):
        self.__yvsi -= unidades
        self.__yvid -= unidades

    def bajar(self,unidades=1):
        self.__yvsi += unidades
        self.__yvid += unidades

    def moverDerecha(self, unidades=1):
        self.__xvsi += unidades
        self.__xvid += unidades

    def moverIzquierda(self, unidades=1):
        self.__xvsi -= unidades
        self.__xvid -= unidades
