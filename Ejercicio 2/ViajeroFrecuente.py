class ViajeroFrecuente:
    __num_viajero = 0
    __dni = 0
    __nombre = ""
    __apellido = ""
    __millas_acum = 0.0

    def __init__(self, nv, dni, nom, ape, mac):
        self.__num_viajero = nv
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__millas_acum = mac

    def __str__(self):
        return f"{self.__num_viajero}     {self.__dni}     {self.__nombre}     {self.__apellido}     {self.__millas_acum}"

    def getNumero(self):
        return self.__num_viajero
    
    def cantidadTotaldeMillas(self):
        return self.__millas_acum

    def acumularMillas(self, cantm):
        self.__millas_acum = self.__millas_acum+cantm
        return self.__millas_acum

    def canjearMillas(self, cantm):
        if cantm <= self.__millas_acum:
            self.__millas_acum -= cantm
            return self.__millas_acum
        else:
            print("No cuenta con la cantidad suiciente de millas")
        