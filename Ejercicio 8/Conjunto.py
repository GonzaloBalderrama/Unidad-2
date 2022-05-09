class Conjunto:
    __elementos = []

    def __init__(self, elementos):
        self.__elementos = elementos

    def getElementos(self):
        return self.__elementos

    def __add__(self, conjunto):
        resultado = self.__elementos
        for i in conjunto.getElementos():
            if not (i in resultado):
                resultado.append(i)
        return resultado

    def __sub__(self, conjunto):
        resultado = []
        for i in self.__elementos:
            if not (i in conjunto.getElementos()):
                resultado.append(i)
        return resultado

    def __eq__(self, conjunto):
        ban = True
        i = 0
        while ban and i<len(self.__elementos):
            if not (self.__elementos[i] in conjunto.getElementos()):
                ban = False
            i +=1
        return ban