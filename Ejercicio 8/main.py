from Conjunto import Conjunto

if __name__=="__main__":
    a = [1,2,3,4]
    b = [1,2,5,6]
    conjuntoA = Conjunto(a)
    conjuntoB = Conjunto(b)

    print("\n**** Conjuntos iniciales ****")
    print(f"Conjunto A={a}")
    print(f"Conjunto B={b}")

    print("\n**** Unión de los conjuntos A y B ****")
    conjuntoC= conjuntoA+conjuntoB
    print(conjuntoC)

    print("\n**** Diferencia entre los conjuntos A y B ****")
    conjuntoC= conjuntoA-conjuntoB
    print(conjuntoC)

    print("\n**** Probar igualdad entre los conjuntos A y B ****")
    if conjuntoA==conjuntoB:
        print("Los conjuntos son iguales")
    else:
        print("Los conjuntos son diferentes")