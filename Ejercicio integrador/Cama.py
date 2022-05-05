from datetime import datetime

class Cama:
    __idCama = None
    __habitacion = None
    __estado = False
    __apellidoNombre = None
    __diagnostico = None
    __observaciones = None
    __fechaInternacion = None
    __fechaAlta = None

    def __init__(self, id, hab, est, aN, diag, obs, fint, falta):
        self.__idCama = id
        self.__habitacion = hab
        self.__estado = est
        self.__apellidoNombre = aN
        self.__diagnostico = diag
        self.__observaciones = obs
        self.__fechaInternacion = fint
        self.__fechaAlta = falta

    def __str__(self):
        return f"{self.__apellidoNombre}     {self.__idCama}    {self.__habitacion}    {self.__diagnostico}    {self.__fechaInternacion}    {self.__observaciones}"
    
    def getAyN(self):
        return self.__apellidoNombre
    
    def getID(self):
        return self.__idCama

    def getEstado(self):
        return self.__estado
    
    def getHab(self):
        return self.__habitacion
    
    def getDiag(self):
        return self.__diagnostico
    
    def getFechaI(self):
        return self.__fechaInternacion
    
    def getFechaA(self):
        return self.__fechaAlta
    
    def actualizarAlta(self):
        fecha = datetime.now()
        self.__fechaAlta = str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)
        self.__estado = False
