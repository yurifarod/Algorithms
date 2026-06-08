import random

'''
Abstracao de uma mochila
Temos ai uma relacao de peso e valor do produto!
'''

itens = [
    (2, 10),
    (3, 15),
    (5, 25),
    (7, 35),
    (1, 5),
    (4, 20)
]

CAPACIDADE = 15

'''
Parametros do ACO
'''
NUM_FORMIGAS = 30
ITERACOES = 200

ALPHA = 1.0
BETA = 2.0

RHO = 0.10

Q = 3

feromonio = [1.0 for _ in itens]

melhor_solucao = None
melhor_valor = 0

'''
Sorteia um candidato proporcionalmente ao seu nível de atratividade (peso).
'''
def selecionar_item(candidatos, pesos):

    soma = sum(pesos)
    if soma == 0:
        return random.choice(candidatos)
    r = random.uniform(0, soma)
    acumulado = 0
    
    for item, peso in zip(candidatos, pesos):
        acumulado += peso
        if acumulado >= r:
            return item

    return candidatos[-1]

for iteracao in range(ITERACOES):

    solucoes = []

    for _ in range(NUM_FORMIGAS):

        peso_total = 0
        valor_total = 0

        solucao = [0] * len(itens)

        disponiveis = list(range(len(itens)))

        while True:

            candidatos = []
            atratividades = []

            for i in disponiveis:

                peso, valor = itens[i]

                if peso_total + peso <= CAPACIDADE:

                    heuristica = valor / peso

                    atratividade = ((feromonio[i] ** ALPHA) * (heuristica ** BETA))

                    candidatos.append(i)
                    atratividades.append(atratividade)

            if not candidatos:
                break

            escolhido = selecionar_item(candidatos,atratividades)

            solucao[escolhido] = 1

            peso, valor = itens[escolhido]

            peso_total += peso
            valor_total += valor

            disponiveis.remove(escolhido)



        solucoes.append((solucao, valor_total))

        # melhor global
        if valor_total > melhor_valor:

            melhor_valor = valor_total
            melhor_solucao = solucao.copy()

    '''
    Evaporação
    '''

    for i in range(len(feromonio)):
        feromonio[i] *= (1 - RHO)

        # evita zerar
        if feromonio[i] < 0.01:
            feromonio[i] = 0.01

    '''
    Escolho a melhor solução para fazer o deposito
    '''

    melhor_iteracao, valor_iteracao = max(solucoes,key=lambda x: x[1])
    deposito = Q * (valor_iteracao / melhor_valor)

    for i in range(len(melhor_iteracao)):

        if melhor_iteracao[i] == 1:
            feromonio[i] += deposito


print("Melhor solução encontrada")

print("Vetor binário:")
print(melhor_solucao)

print("Valor total:", melhor_valor)

peso_final = 0

print("Itens escolhidos:")

for i, gene in enumerate(melhor_solucao):

    if gene == 1:

        peso, valor = itens[i]

        peso_final += peso

        print(
            f"Item {i+1}: "
            f"peso={peso}, "
            f"valor={valor}"
        )

print("Peso total:", peso_final)
print("Capacidade :", CAPACIDADE)

print("Feromônios finais:")
for i, f in enumerate(feromonio):
    print(f"Item {i+1}: {f:.3f}")