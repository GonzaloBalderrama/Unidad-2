import csv
from planahorro import PlanAhorro
class Manejador:
    lista=[]
    def __init__(self):
        self.__lista=[]
    def leerArchivo(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            c=fila[0]
            m=fila[1]
            ve=fila[2]
            va=float(fila[3])
            plane=PlanAhorro(c,m,ve,va)
            PlanAhorro.setCantiCuo(int(fila[4]))
            PlanAhorro.setCantiPag(int(fila[5]))
            self.__lista.append(plane)
        archivo.close()
    def Modifica(self):
        for obj in self.__lista:
            print(obj)
            valor=float(input('Ingrese nuevo valor del vehiculo: '))
            obj.setValor(valor)
            print('\n\n')  
    def Valor(self):
        print('------------------------------------------')
        valor=float(input('Ingrese un valor: '))
        for obj in self.__lista:
            valorobj=(obj.getValor()/obj.getCantiCuo())+obj.getValor()*0.10 
            if(valor > valorobj ):
                print('Codigo del plan:{}  Modelo:{}   Version:{}'.format(obj.getCodigo(),obj.getModelo(),obj.getVersion()))
        print('------------------------------------------')    
    def Licitar(self):
        print('------------------------------------------')  
        for obj in self.__lista:
            valorobj=(obj.getValor()/obj.getCantiCuo())+obj.getValor()*0.10 
            print('Codigo del plan:{}   Cuotas a pagar:{:.2f}'.format(obj.getCodigo(),valorobj*PlanAhorro.getCantiPag()))
        print('------------------------------------------') 
    def ModificaCuotas(self):
        codigo=input('Ingrese codigo de plan:')
        print('------------------------------------------')  
        for obj in self.__lista:
            if(codigo==obj.getCodigo()):
                print(PlanAhorro.getCantiPag())
                print('------------------------------------------')  
                modi=input('Ingrese la modificacion de cantidad de cuotas pagas:')
                PlanAhorro.setCantiPag(modi)