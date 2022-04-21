class Email:
    __idCuenta = ''
    __dominio = ''
    __tipo_de_dominio = ''
    __contra = ''

    def __init__(self, idc='', dom='', tdd='', con='1234'):
        self.__idCuenta = idc
        self.__dominio = dom
        self.__tipo_de_dominio = tdd
        self.__contra = con
    
    def __str__(self):
        return "%s@%s.%s" % (self.__idCuenta, self.__dominio, self.__tipo_de_dominio)    
        
    def retornaEmail(self):
        return (f'{self.__idCuenta}@{self.__dominio}.{self.__tipo_de_dominio}')

    def getID(self):
        return self.__idCuenta

    def getDominio(self):
        return self.__dominio

    def cambiarContrasenia(self):
        ban = True
        while ban == True:
            contra = input("Ingrese contraña actual: ")
            if contra == self.__contra:
                self.__contra = input("Ingrese su nueva contraseña: ")
                print("¡Su contraseña se actualizò correctamente!")
                ban = False
            else:
                print("La contraseña ingresada no es vàlida")

    def crearEmail(self):
        ban= True
        while ban == True: 
            e= input("Ingrese su direcciòn de correo: ")
            try:
                e.index("@")
                e.index(".")
                self.__idCuenta = e[:e.find("@")]
                self.__dominio = e[e.find("@")+1:e.find(".")]
                self.__tipo_de_dominio = e[e.find(".")+1:]
                print(self.__idCuenta)
                print(self.__dominio)
                print(self.__tipo_de_dominio)
                ban = False
            except:
                print("¡El correo ingresado en invalido!")