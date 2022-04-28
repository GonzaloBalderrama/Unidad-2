import code
from operator import mod
from tabnanny import verbose


class PlanAhorro:
    __codigo = 0
    __modelo = ""
    __version = ""
    __valor = 0
    cant_cuotas = 60
    cc_pagas = 10

    def __init__(self, cod, mod, ver, val):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valor = val

    def __str__(self):
        return f'{self.__codigo}    {self.__modelo}    {self.__version}    {self.__valor}    {self.cant_cuotas}    {self.cc_pagas}'

    def importe(self):
        return (self.__valor/self.__cant_cuotas)+self.__valor*0.10
    
