from dis import dis
from ManejadorCama import ManejadorCama

if __name__ == '__main__':
    listaCamas = ManejadorCama()
    listaCamas.crearC()
    print(listaCamas)
    print("******************************* Clínica Sanitos *******************************")
    nom = input("Ingrese el apellido y nombre de paciente para dar el alta --> ")
    listaCamas.buscarPaciente(nom)
    diagnostico = input("Ingrese el dignostico para mostrar pacientes internados --> ")
    listaCamas.listarPorDiagnostico(diagnostico)
    