class Medicamento:
    __idCama = None
    __idMedicamento = None
    __nombre = None
    __monodroga = None
    __presentación = None
    __cantapli = None
    __preciot = None

    def __init__(self, idc, idm, nom, monod, pres, cant, ptotal):
        self.__idCama = idc
        self.__idMedicamento = idm
        self.__nombre = nom
        self.__monodroga = monod
        self.__presentación = pres
        self. __cantapli = cant
        self.__preciot = ptotal

    def __str__(self):
        return f"{self.__idCama}   {self.__idMedicamento}   {self.__nombre}   {self.__monodroga}   {self.__presentación}   {self.__cantapli}   {self.__preciot}"
        
    def getIdCama(self):
        return self.__idCama
    
    def getNombre(self):
        return self.__nombre
    
    def getMonodroga(self):
        return self.__monodroga
    
    def getPresentacion(self):
        return self.__presentación

    def getCantidad(self):
        return self.__cantapli

    def getPrecio(self):
        return self.__preciot
