class Email:
    __idCuenta = ''
    __dominio = ''
    __tipo_de_dominio = ''
    __contra = ''

    def __init__(self, idc='', dom='', tdd='', con=''):
        self.__idCuenta = idc
        self.__dominio = dom
        self.__tipo_de_dominio = tdd
        self.__contra = con
        
    def retornaEmail(self):
        return print(f'{self.__idCuenta}@{self.__dominio}.{self.__tipo_de_dominio}')
    def setDom(self,dato):
        self.__dominio=dato
    def getDominio(self):
        return self.__dominio

    def crearCuenta(self, nom, e):
        nom= input("Ingrese su nombre:")
        if ((e.find("@") != -1) & (e.find(".") != -1)):
            otroEmail = self.__init__(e[:e.find('@')], e[e.find('@')+1:e.find('.')],e[e.find('.')+1:], contra=input('ingrese la contraseña para el nuevo objeto:'))
        otroEmail.__idCuenta = input('Ingrese ID de su cuenta: ')
        otroEmail.__dominio = input('Ingrese el dominio de su cuenta: ')
        otroEmail.__tipo_de_dominio  = input('Ingrese tipo de dominio de su cuenta: ')
        

if __name__ == '__main__':
    unEmail = Email('gonzalo', 'gmail', 'com', '1234')
    unEmail.retornaEmail()
    Email1 = Email(input("Ingrese su Id: "), input('Ingrese dominio'), input("Ingrese el tipo de dominio: ", ""  ))
    nombre = input("Ingrese su nombre: ")Gon

    print(f'dom {Email1.getDominio()}')
    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {Email1.__idCuenta}@{Email1.__dominio}.{Email1.__tipo_de_dominio}>.")


    
