import random


def criarPar(conjuntoA, conjuntoB, p):
    parRelacao = []
    matriz =[]
    for i in range(len(conjuntoA)):
        aux1 = []
        for j in range(len(conjuntoB)):
            aux1.append(0)
        matriz.append(aux1)
    for i in range(len(conjuntoA)):
        count = 0
        for j in range(len(conjuntoB)):
            rng = random.randrange(0, len(conjuntoB))
            if count < p:
                aux = []
                aux.append(conjuntoA[i])
                aux.append(conjuntoB[rng])
                parRelacao.append(aux)
                matriz[i][rng]=1
                count=count+1
            else:
                break
    return parRelacao, matriz


def relacaoComposta(matrizRelacao1, matrizRelacao2):
    matrizResultado = []
    for i in range(0,len(matrizRelacao1)):
        temp=[]
        for j in range(0,len(matrizRelacao2[0])):
            s = 0
            for k in range(0,len(matrizRelacao1[0])):
                s += matrizRelacao1[i][k]*matrizRelacao2[k][j]
            temp.append(s)
        matrizResultado.append(temp)
    return matrizResultado


def imprimirMatriz(matriz):
    for coluna in matriz:
        print(coluna)


with open('inputRelação.txt') as file:
    lines = file.readlines()
    conjunto1 = lines[0].split()
    conjunto2 = lines[1].split()
    conjunto3 = lines[2].split()


n = 2
m = 3

relacaoAB, matrizAB = criarPar(conjunto1, conjunto2, n)
relacaoBC, matrizBC  = criarPar(conjunto2, conjunto3, m)

matrizComposta = relacaoComposta(matrizAB, matrizBC)
print("")
print("Matriz da relação AB")
imprimirMatriz(matrizAB)
print("")
print("Matriz da relação BC")
imprimirMatriz(matrizBC)
print("")
print("Matriz da relação composta")
imprimirMatriz(matrizComposta)