import random
'''
Abstracao de uma mochila
Temos ai uma relacao de peso e valor do produto!
'''
itens = [[2, 10],
	    [3, 15],
	    [5, 25],
	    [7, 35],
	    [1, 5],
	    [4, 20]]

CAPACIDADE = 15

'''
O gene: [1, 0, 1, 1, 0, 0]
Indica se os produtos, em ordem, foram selecionados ou nao

Item 1 -> Sim
Item 2 -> Não
Item 3 -> Sim
Item 4 -> Sim
Item 5 -> Não
Item 6 -> Não
'''

def fitness(individuo):
    peso_total = 0
    valor_total = 0

    for gene, item in zip(individuo, itens):
        if gene == 1:
            peso_total += item[0]
            valor_total += item[1]

    if peso_total > CAPACIDADE:
        return 0

    return valor_total

def gerar_individuo():
    return [random.randint(0, 1) for _ in range(len(itens))]

def gerar_populacao(tamanho):
    return [gerar_individuo() for _ in range(tamanho)]

def crossover(pai1, pai2):
    corte = random.randint(1, len(pai1)-1)

    filho1 = pai1[:corte] + pai2[corte:]
    filho2 = pai2[:corte] + pai1[corte:]

    return filho1, filho2

def mutacao(individuo, taxa=0.05):

    for i in range(len(individuo)):
        if random.random() < taxa:
            individuo[i] = 1 - individuo[i]

    return individuo


POPULACAO = 20
GERACOES = 100

populacao = [gerar_individuo() for _ in range(POPULACAO)]

for _ in range(GERACOES):

    populacao.sort(key=fitness, reverse=True)

    '''
    Escolhemos por elitismo a melhor solucao para o "cruzamento"
    '''
    nova_pop = populacao[:2]

    while len(nova_pop) < POPULACAO:

        pai1 = random.choice(populacao[:10])
        pai2 = random.choice(populacao[:10])

        filho1, filho2 = crossover(pai1, pai2)

        nova_pop.append(mutacao(filho1))

        if len(nova_pop) < POPULACAO:
            nova_pop.append(mutacao(filho2))

    populacao = nova_pop

melhor = max(populacao, key=fitness)

print("Melhor solução:", melhor)
print("Fitness:", fitness(melhor))