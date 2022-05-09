from manejador import Manejador
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher= {'1':self.opcion1, '2':self.opcion2, '3':self.opcion3, '4':self.opcion4, '5':self.salir}
    def opcion(self,op,manejador):
        func=self.__switcher.get(op,lambda: print('Opcion no valida'))
        if(op=='1' or op=='2' or op=='3' or op=='4'):
            func(manejador)
        else:
            func()
    def opcion1(self,manejador):
        if type(manejador)==Manejador:
            manejador.Modifica()      
    def opcion2(self,manejador):
        if type(manejador)==Manejador:
            manejador.Valor()
    def opcion3(self,manejador):
        if type(manejador)==Manejador:
            manejador.Licitar()
    def opcion4(self,manejador):
        if type(manejador)==Manejador:
            manejador.ModificaCuotas()
    def salir(self):
        print('terminado!')