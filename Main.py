def pertence(conjunto1, x):
    for j in range(len(conjunto1)):
        if x == conjunto1[j]:
            return True
    return False


def contido(conjunto1, conjunto2):
    count = 0
    for i in range(len(conjunto2)):
        if pertence(conjunto1, conjunto2[i]):
            count = count + 1
    return count


def uniao(conjunto1, conjunto2):
    resultado = []
    resultado.extend(conjunto1)
    for i in range(len(conjunto2)):
        if not pertence(conjunto1, conjunto2[i]):
            resultado.append(conjunto2[i])
    return resultado


def intersecao(conjunto1, conjunto2):
    resultado = []
    for i in range(len(conjunto1)):
        if pertence(conjunto2, conjunto1[i]):
            resultado.append(conjunto1[i])
    return resultado


def produtoCartesiano(conjunto1, conjunto2):
    resultado = []
    for i in range(len(conjunto1)):
        for j in range(len(conjunto2)):
            aux = []
            aux.append(conjunto1[i])
            aux.append(conjunto2[j])
            resultado.append(aux)
    return resultado


def combinacao(conjunto, tamanho):
    if tamanho == 0:
        return [[]]
    resultado = []
    for i in range(len(conjunto)):
        aux = conjunto[i]
        remLst = conjunto[i + 1:]
        for i in combinacao(remLst, tamanho - 1):
            resultado.append([aux] + i)
    return resultado


def conjuntoDasPartes(conjunto):
    conjuntao = []
    for i in range(len(conjunto)):
        conjuntao.extend(combinacao(conjunto, len(conjunto) - i))
    conjuntao.extend([[]])
    return conjuntao


escolha = input("Digite 1 para ler um arquivo ou 2 para entrar os elementos de um conjunto manualmente: ")
if escolha == '1':
    with open('input.txt') as file:
        lines = file.readlines()
        conjunto1 = lines[0].split()
        conjunto2 = lines[1].split()
elif escolha == '2':
    aux = input("Digite o primeiro conjunto: ")
    conjunto1 = aux.split()
    aux = input("Digite o segundo conjunto: ")
    conjunto2 = aux.split()
    print(conjunto1)
    print(conjunto2)
print("")
print("")
print("Verificando se os elementos do Conjunto 2 pertencem ao Conjunto 1")
for i in range(len(conjunto2)):
    if pertence(conjunto1, conjunto2[i]):
        print("O elmento " + conjunto2[i] + " do Conjunto 2 pertence ao Conjuto 1")
    else:
        print("O elmento " + conjunto2[i] + " do Conjunto 2 não pertence ao Conjuto 1")

print("")
print("")
print("Verificando se o Conjunto 2 está contido no 1")
count = contido(conjunto1, conjunto2)
if count == len(conjunto2):
    if len(conjunto1) == len(conjunto2):
        print("O conjunto 2 está contido no Conjunto 1")
    else:
        print("O conjunto 2 está contido propriamente no Conjunto 1")
else:
    print("O conjunto 2 não está contido no Conjunto 1")

print("")
print("")
print("Realizando a União entre o Conjunto 1 e o Conjunto 2")
print(uniao(conjunto1, conjunto2))

print("")
print("")
print("Realizando a Interseçao entre o Conjunto 1 e o Conjunto 2")
print(intersecao(conjunto1, conjunto2))

print("")
print("")
print("Realizando o Produto Cartesiano entre o Conjunto 1 e o Conjunto 2")
print(produtoCartesiano(conjunto1, conjunto2))

print("")
print("")
print("Realizando o Conjunto das Partes do Conjunto 2")
print(conjuntoDasPartes(conjunto2))
