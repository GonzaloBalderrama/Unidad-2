class PlanAhorro:
    __codigo=0
    __modelo=''
    __version=0
    __valor=0.0
    #Variables de clase
    __cantiCuotas=0
    __cantiPagas=0
    def __init__(self,codigo,modelo,version,valor):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
    def __str__(self):
        return ('codigo:{} \t modelo:{} \t version:{}').format(self.__codigo,self.__modelo,self.__version)
    def setValor(self,val):
        self.__valor=val
    def getValor(self):
        return self.__valor
    def getCodigo(self):
        return self.__codigo
    def getModelo(self):
        return self.__modelo
    def getVersion(self):
        return self.__version
    @classmethod
    def setCantiCuo(cls,cuota):
        cls.__cantiCuotas=cuota
    @classmethod
    def setCantiPag(cls,paga):
        cls.__cantiPagas=paga
    @classmethod
    def getCantiCuo(cls):
        return cls.__cantiCuotas
    @classmethod
    def getCantiPag(cls):
        return cls.__cantiPagas