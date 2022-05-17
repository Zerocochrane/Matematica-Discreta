def igualdade(conjuntoA, conjuntoB):
    matriz = []

    for i in range(len(conjuntoA)):
        aux1 = []
        for j in range(len(conjuntoB)):
            aux1.append(0)
        matriz.append(aux1)
    for i in range(len(conjuntoA)):
        for j in range(len(conjuntoB)):
            if conjuntoA[i] == conjuntoB[j]:
                matriz[i][j] = 1

    return matriz


def relacaoComposta(matrizRelacao1, matrizRelacao2):
    matrizResultado = []
    for i in range(0, len(matrizRelacao1)):
        temp = []
        for j in range(0, len(matrizRelacao2[0])):
            s = 0
            for k in range(0, len(matrizRelacao1[0])):
                s += matrizRelacao1[i][k] * matrizRelacao2[k][j]
            temp.append(s)
        matrizResultado.append(temp)
    return matrizResultado


def imprimirMatriz(matriz):
    for coluna in matriz:
        print(coluna)


with open('inputRelacao.txt') as file:
    lines = file.readlines()
    conjunto1 = lines[0].split()
    conjunto2 = lines[1].split()
    conjunto3 = lines[2].split()

escolha = input("Digite qual relacao deseja verificar: ")

if escolha == '=':
    matrizAB = igualdade(conjunto1, conjunto2)
    matrizBC = igualdade(conjunto2, conjunto3)
    resultado = relacaoComposta(matrizAB,matrizBC)

    imprimirMatriz(resultado)
